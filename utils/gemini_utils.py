# import google.generativeai as genai
from google import genai
from google.genai import types
# Configure Gemini API
import os
# import google.generativeai as genai

os.environ["GOOGLE_API_KEY"] = "api_KEY"

# genai.configure() 
GOOGLE_API_KEY="AIzaSyBvE82VYWYZknp0g31a8WB6WvFQV_YbimE"
API_KEY = GOOGLE_API_KEY
# genai.configure(api_key=API_KEY)
# Initialize the Gemini model

#model = genai.GenerativeModel('gemini-2.0-flash')
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
