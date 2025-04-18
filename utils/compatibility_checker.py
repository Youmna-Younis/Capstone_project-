import google.generativeai as genai
import json

from utils.gemini_utils import generate_response
from utils.data_extractor import parse_llm_response
def check_compatibility(resume_data, job_description):
    # Construct the prompt with explicit JSON formatting instructions
    prompt = f'''
    You are an AI bot that checks the compatibility of a resume with a job description.
    Your task is to compare the following resume with the given job description, and then:
    1. Check if the resume matches the requirements of the job description. Provide a compatibility score (0-100).
    2. Extract the following information from the resume in JSON format:
        - Full Name
        - Email ID
        - GitHub Portfolio (if available)
        - LinkedIn ID (if available)
        - Employment Details (roles, companies, and dates)
        - Technical Skills (list specific skills)
        - Soft Skills (list relevant skills)
    3. Generate 3 interview questions based on the resume content and the job description.

    Please return your response strictly in JSON format. Example:
    {{
        "compatibility_score": 85,
        "resume_details": {{
            "full_name": "John Doe",
            "email_id": "john.doe@example.com",
            "github_portfolio": "https://github.com/johndoe",
            "linkedin_id": "https://www.linkedin.com/in/johndoe",
            "employment_details": [
                {{
                    "role": "Software Engineer",
                    "company": "Tech Corp",
                    "dates": "Jan 2020 - Dec 2022"
                }}
            ],
            "technical_skills": ["Python", "JavaScript", "SQL"],
            "soft_skills": ["Communication", "Teamwork"]
        }},
        "interview_questions": [
            "Question 1...",
            "Question 2...",
            "Question 3..."
        ]
    }}
    '''

    # Combine resume_data, job_description, and prompt into a single string
    input_text = f"""
    Resume Data:
    {resume_data}

    Job Description:
    {job_description}

    Instructions:
    {prompt}
    """



    response = generate_response(input_text)
    print(f"RE:{response}")
    data=parse_llm_response(response)

    return data






















