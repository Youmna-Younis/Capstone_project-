import google.generativeai as genai

# Configure Gemini API
GEMINI_API_KEY="AIzaSyBvE82VYWYZknp0g31a8WB6WvFQV_YbimE"
API_KEY = GEMINI_API_KEY
genai.configure(api_key=API_KEY)
# Initialize the Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')


def generate_response(prompt):
    """
    Generates a response using Gemini.
    """
    response = model.generate_content(prompt)
    return response.text.strip()