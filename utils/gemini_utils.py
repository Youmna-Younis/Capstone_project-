# import google.generativeai as genai
from google import genai
from google.genai import types
# Configure Gemini API
import os
from dotenv import load_dotenv
# import google.generativeai as genai
load_dotenv()
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")


client = genai.Client(api_key=GOOGLE_API_KEY)

def generate_response(prompt):
    """
    Generates a response using Gemini.
    """
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt)

    # response = model.generate_content(prompt)
    return response.text.strip()
def Generate_response(prompt,config):
    """
    Generates a response using Gemini.
    """
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
    config=config
    )

    # response = model.generate_content(prompt)
    return response.text.strip()


