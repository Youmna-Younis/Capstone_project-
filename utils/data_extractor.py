import PyPDF2
import re
import PyPDF2
import logging
from typing import Dict
from utils.gemini_utils import generate_response
def Extract_data_from_pdf(pdf_file_path: str) -> Dict:
    """
    Extracts key data from a PDF resume using an LLM model.

    Args:
        pdf_file_path (str): The path to the PDF file.
        llm_model: An instance of an LLM model capable of processing text.

    Returns:
        dict: Extracted data from the resume in JSON format.
    """
    try:
        # Step 1: Read the PDF file and extract its text
        with open(pdf_file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

        # Step 2: Craft a prompt for the LLM to extract structured data in JSON format
        prompt = f"""
        Analyze the following resume text and extract the following information in JSON format:
        {{
            "full_name": "The full name of the candidate",
            "email": "The email address of the candidate",
            "skills": ["A list of skills mentioned in the resume"]
        }}

        Resume Text:
        {text}

        Ensure the response is valid JSON and adheres to the structure provided above.
        """

        # Step 3: Generate the response from the LLM
        response = generate_response(prompt)

        # Step 4: Parse the LLM's response into a dictionary
        extracted_data = parse_llm_response(response)

    except Exception as e:
        logging.error(f"Error extracting data from PDF: {str(e)}")
        raise Exception(f"Failed to extract data from PDF: {str(e)}")

    return extracted_data


def parse_llm_response(response: str) -> Dict:
    """
    Parses the LLM's response into a structured dictionary.

    Args:
        response (str): The raw response from the LLM.

    Returns:
        dict: Parsed data in JSON format.
    """
    import json

    try:
        # Step 1: Remove Markdown-style backticks
        cleaned_response = re.sub(r"^```json\s*|\s*```$", "", response.strip(), flags=re.MULTILINE)

        # Attempt to parse the response as JSON
        parsed_data = json.loads(cleaned_response)

        # # Validate that the required fields are present
        # required_fields = ["full_name", "email", "skills"]
        # for field in required_fields:
        #     if field not in parsed_data:
        #         raise KeyError(f"Missing required field in LLM response: {field}")

        return parsed_data

    except json.JSONDecodeError:
        raise ValueError("LLM response is not valid JSON.")
