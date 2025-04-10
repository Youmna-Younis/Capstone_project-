import google.generativeai as genai
import json

def check_compatibility(resume_data, job_description, api_key):
    prompt = f'''
    You are an AI bot that checks the compatibility of a resume with a job description. 
    Your task is to compare the following resume with the given job description, and then:
    1. Check if the resume matches the requirements of the job description.
    2. Extract the following information from the resume:
        - Full Name
        - Email ID
        - GitHub Portfolio (if available)
        - LinkedIn ID (if available)
        - Employment Details (roles, companies, and dates)
        - Technical Skills (list specific skills)
        - Soft Skills (list relevant skills)
    3. Generate 3 interview questions based on the resume content and the job description.

    Resume Data:
    {resume_data}

    Job Description:
    {job_description}
    '''
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0')
    response = model.generate_content([resume_data, job_description, prompt])

    data = response.text.strip()

    try:
        json_data = json.loads(data)
        return json_data
    except Exception as e:
        return {"error": "Failed to parse the response", "details": str(e)}

