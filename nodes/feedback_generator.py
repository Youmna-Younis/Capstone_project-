from langchain_core.runnables import RunnableLambda
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langgraph.graph import StateGraph

GOOGLE_API_KEY = 'YOUR_API_KEY'

gemini_llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# A callable that uses Gemini to generate feedback
def generate_feedback(inputs):
    
    question = inputs["question"]
    answer = inputs["answer"]
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
