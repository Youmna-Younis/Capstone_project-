def generate_summary(extracted_data):
    # Get technical skills, default to empty list if not available
    technical_skills = ', '.join(extracted_data.get('technical_skills', []))
    if not technical_skills:
        technical_skills = "No technical skills listed"
    
    # Get employment details, default to empty list if not available
    employment_details = ', '.join([job['role'] for job in extracted_data.get('employment_details', [])])
    if not employment_details:
        employment_details = "No work experience listed"

    # Get soft skills, default to empty list if not available
    soft_skills = ', '.join(extracted_data.get('soft_skills', []))
    if not soft_skills:
        soft_skills = "No soft skills listed"

    # Generate summary
    summary = f"Applicant {extracted_data.get('full_name', 'No name provided')} is skilled in {technical_skills}. "
    summary += f"They have experience in roles such as {employment_details}. "
    summary += f"Their soft skills include {soft_skills}."
    
    return summary
