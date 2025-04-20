from langchain_core.runnables import RunnableLambda
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.prompts import PromptTemplate
from langchain_core.prompts import PromptTemplate

from langgraph.graph import StateGraph
import re
from langchain_core.messages.utils import get_buffer_string
import re
import json
import os
from utils.gemini_utils import *
from utils.state_schema import InterviewPreparationState

# GOOGLE_API_KEY = 'YOUR_API_KEY'

gemini_llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# A callable that uses Gemini to generate feedback
def generate_feedback(inputs):
    
    question = inputs["questions"]
    answer = inputs["candidate_responses"]
    traits = inputs.get("desired_traits", "professionalism, clarity, problem-solving")

    feedback_prompt = PromptTemplate.from_template(
    """
    You are an HR interviewer. Evaluate the candidate’s answer to the question below.

    Question: {question}
    Answer: {answer}
    Desired Traits: {desired_traits}

    Provide detailed, constructive feedback focusing on strengths and improvement areas.
    """)
    
    formatted_prompt = feedback_prompt.format(
        question=question,
        answer=answer,
        desired_traits=traits
    )

    # Invoke Gemini model
    feedback = gemini_llm.invoke(formatted_prompt)
    return {"feedback": feedback}

def parse_feedback(feedback):
    # Split the feedback into sections
    sections = re.split(r'\*\*', feedback)

    # Initialize the dictionary
    feedback_dict = {}

    # Initialize variables to keep track of the current section and subsection
    current_section = None
    current_subsection = None

    # Iterate through the sections
    for section in sections:
        section = section.strip()
        if not section:
            continue

        # Check if the section is a main heading
        if ':' in section:
            current_section = section.split(':')[0].strip()
            value = section.split(':', 1)[1].strip()
            feedback_dict[current_section] = value
            current_subsection = None
        elif section.startswith('*'):
            # Check if the section is a subsection
            subsection_match = re.match(r'\*\s*(.+)', section)
            if subsection_match:
                subsection_key = subsection_match.group(1).strip()
                if current_subsection is None:
                    current_subsection = {}
                    feedback_dict[current_section] = current_subsection
                current_subsection[subsection_key] = section.split(':', 1)[1].strip() if ':' in section else ''
        else:
            # Add the section to the current subsection or section
            if current_subsection is not None:
                current_subsection[current_section] = section
            else:
                feedback_dict[current_section] += ' ' + section

    return feedback_dict

def clean_text(input_dict):
    cleaned_dict = {}
    for key, value in input_dict.items():
        if isinstance(value, str):
            # Remove actual newlines, escaped newlines, and backslashes
            value = value.replace('\n', ' ').replace('\\n', ' ').replace('\\', '')
            # Keep only letters, digits, periods, commas, double quotes, and spaces
            cleaned_value = re.sub(r'[^a-zA-Z0-9.,\" ]+', '', value)
            # Collapse multiple spaces into one
            cleaned_value = re.sub(r'\s+', ' ', cleaned_value).strip()
            cleaned_dict[key] = cleaned_value
        else:
            cleaned_dict[key] = value
    return cleaned_dict

def report_generator(feedback_message):
    feedback_dict = parse_feedback(feedback_message)
    cleaned = clean_text(feedback_dict)
    # report = json.dumps(, indent=4)
    # # with open("report.json", "w") as outfile:
    #     outfile.write(report)
def generate_interview_report(state: InterviewPreparationState) -> str:
    candidate_info = state.get("candidate_info", {})
    questions = state.get("questions", [])
    responses = state.get("candidate_responses", [])
    evaluations = state.get("evaluations", [])

    report_lines = []

    # Header
    report_lines.append("📋 INTERVIEW SUMMARY REPORT")
    report_lines.append("=" * 40)

    # Candidate Info
    report_lines.append("\n👤 Candidate Info:")
    for key, value in candidate_info.items():
        report_lines.append(f"- {key.capitalize()}: {value}")

    # Q&A Section
    report_lines.append("\n🗣️ Interview Q&A:")
    for i, (q, a) in enumerate(zip(questions, responses), 1):
        report_lines.append(f"\nQuestion {i}: {q}")
        report_lines.append(f"Answer {i}: {a}")

    # Evaluation Section
    report_lines.append("\n📊 Evaluation Summary:")
    for i, eval_entry in enumerate(evaluations[1:], 1):  # Skip placeholder class at index 0
        eval_data = eval_entry.get("evaluation", {})
        summary = eval_data.get("summary", "No summary available.")
        score = eval_data.get("score", "N/A")
        impression = eval_data.get("overall_impression", "N/A")

        report_lines.append(f"\nEvaluation Round {i}:")
        report_lines.append(f"- Score: {score}")
        report_lines.append(f"- Impression: {impression}")
        report_lines.append(f"- Summary: {summary}")

    # Final Impression
    final_impression = evaluations[-1].get("evaluation", {}).get("overall_impression", "Neutral") \
        if isinstance(evaluations[-1], dict) else "Neutral"
    
    report_lines.append("\n✅ Final Overall Impression:")
    report_lines.append(f"{final_impression}")

    return "\n".join(report_lines)
        