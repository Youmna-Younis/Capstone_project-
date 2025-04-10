# Import Libraries

import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
import logging
from utils.compatibility_checker import check_compatibility
from utils.summary_generator import generate_summary
from utils.interview_questions import get_static_interview_questions
from utils.data_extractor import extract_data_from_pdf

# Load environment 
load_dotenv()

# Load the Google API key from the environment
google_api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=google_api_key)

def parse_resume(state):
    
    resume_file_path = state.get("resume")
    job_description = state.get("job_description")

    if not resume_file_path or not job_description:
        return json.dumps({"error": "Resume file path or job description is missing"})

    try:
        # Step 1: Extract data from the resume (PDF file)
        extracted_data = extract_data_from_pdf(resume_file_path)
    except Exception as e:
        logging.error(f"Error extracting data from resume: {str(e)}")
        return json.dumps({"error": "Failed to extract resume data", "details": str(e)})

    # Step 2: Check compatibility and extract data using the Gemini model
    compatibility_data = check_compatibility(resume_file_path, job_description, google_api_key)

    if "error" in compatibility_data:
        return json.dumps({"error": compatibility_data["error"], "details": compatibility_data["details"]})

    # Step 3: Generate a brief summary of the applicant
    summary = generate_summary(extracted_data)

    # Step 4: Get static interview questions
    static_questions = get_static_interview_questions()

    # Step 5: Combine static questions with dynamic questions from the resume and job description
    dynamic_questions = compatibility_data.get("interview_questions", [])
    all_interview_questions = static_questions + dynamic_questions

    # Step 6: Format output into a structured JSON response
    response = {
        "compatibility_check": compatibility_data["compatibility_check"],
        "extracted_data": extracted_data,
        "summary": summary,
        "interview_questions": all_interview_questions
    }

    # Return the final response as JSON
    return json.dumps(response, indent=4)
