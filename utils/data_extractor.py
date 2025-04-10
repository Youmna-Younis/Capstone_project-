import PyPDF2
import re

def extract_data_from_pdf(pdf_file_path):
    """
    Extracts key data from a PDF resume.

    Args:
        pdf_file_path (str): The path to the PDF file.

    Returns:
        dict: Extracted data from the resume in JSON format.
    """
    extracted_data = {}
    try:
        with open(pdf_file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

            # Extract relevant information from the PDF text
            extracted_data["full_name"] = extract_name_from_text(text)
            extracted_data["email"] = extract_email_from_text(text)
            extracted_data["skills"] = extract_skills_from_text(text)

    except Exception as e:
        raise Exception(f"Failed to extract data from PDF: {str(e)}")

    return extracted_data

def extract_name_from_text(text):
    # Assuming the name is at the beginning
    lines = text.split('\n')
    return lines[0] if lines else "Name not found"

def extract_email_from_text(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else "Email not found"

def extract_skills_from_text(text):
    # Example: Extract skills listed in the resume
    skills = ["Python", "Machine Learning", "SQL", "TensorFlow"]
    return [skill for skill in skills if skill in text]
