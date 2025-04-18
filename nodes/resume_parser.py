# Import Libraries

import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
import logging
from utils.compatibility_checker import check_compatibility
from utils.summary_generator import generate_summary
from utils.interview_questions import get_static_interview_questions
from utils.data_extractor import Extract_data_from_pdf
from utils.state_schema import ResumeParsingState
from utils.gemini_utils import generate_response

# # Load environment 
# load_dotenv()

# # Load the Google API key from the environment
# google_api_key = os.getenv("GOOGLE_API_KEY")


def parse_resume(state: ResumeParsingState) -> ResumeParsingState:
    # Extract required fields from the state
    resume_file_path = state.get("resume")
    job_description = state.get("job_description")

    # Validate input
    if not resume_file_path or not job_description:
        print("Validation failed: Missing resume file path or job description.")
        return {
            **state,
            "error": "Resume file path or job description is missing",
            "stage": "error"
        }

    try:
        # Step 1: Extract data from the resume (PDF file)
        print("Step 1: Extracting data from the resume...")
        extracted_data = Extract_data_from_pdf(resume_file_path)
        print(f"Extracted data: {extracted_data}")

        # Step 2: Check compatibility and extract data using the Gemini model
        print("Step 2: Checking compatibility with the job description...")
        compatibility_data = check_compatibility(extracted_data, job_description)
        print(f"Compatibility data: {compatibility_data}")

        if "error" in compatibility_data:
            print("Error detected in compatibility data.")
            return {
                **state,
                "error": compatibility_data["error"],
                "details": compatibility_data["details"],
                "stage": "error"
            }

        # Step 3: Generate a brief summary of the applicant
        print("Step 3: Generating summary...")
        summary = generate_summary(extracted_data)
        print(f"Generated summary: {summary}")

        # Step 4: Get static interview questions
        print("Step 4: Fetching static interview questions...")
        static_questions = get_static_interview_questions()
        print(f"Static interview questions: {static_questions}")

        # Step 5: Combine static questions with dynamic questions from the resume and job description
        print("Step 5: Combining static and dynamic interview questions...")
        dynamic_questions = compatibility_data.get("interview_questions", [])
        all_interview_questions = static_questions + dynamic_questions
        print(f"All interview questions: {all_interview_questions}")

        # Step 6: Update the state with the parsed data
        print("Step 6: Updating state with parsed data...")
        updated_state = {
            **state,
            "extracted_data": extracted_data,
            "compatibility_check": compatibility_data.get("compatibility_check", ""),
            "summary": summary,
            "interview_questions": all_interview_questions,
            "stage": "ready_for_hr"
        }
        print(f"Updated state: {updated_state}")
        return updated_state

    except Exception as e:
        # Log the error for debugging purposes
        print(f"Exception occurred: {str(e)}")
        logging.error(f"Error extracting data from resume: {str(e)}")

        # Return an error response
        return {
            **state,
            "error": "Failed to extract resume data",
            "details": str(e),
            "stage": "error"
        }