
import os
import json
# import google.generativeai as genai
import logging

from utils.state_schema import ResumeParsingState
from utils.state_schema import InterviewPreparationState
from utils.state_schema import BaseState

def prepare_interview_context(state: ResumeParsingState) -> InterviewPreparationState:
    # Extract relevant fields
    extracted_data = state.get("extracted_data", {})
    compatibility_check = state.get("compatibility_check", "")
    summary = state.get("summary", "")
    interview_questions = state.get("interview_questions", [])

    # Create context for the LLM
    llm_context = f"""
    You are conducting an interview for a candidate with the following profile:
    - Summary: {summary}
    - Skills: {extracted_data.get("skills", "N/A")}
    - Compatibility Check: {compatibility_check}

    Use the following questions as a starting point:
    {json.dumps(interview_questions, indent=2)}

    Generate follow-up questions based on the candidate's responses to make the conversation flow naturally.
    """
    print(f"LLM context :{llm_context}")
    return {
        **state,
        "llm_context": llm_context,
        "messages": [],

        "stage": "ready_for_interview"
    }