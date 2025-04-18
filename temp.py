import google.generativeai as genai

# Configure Gemini API
GEMINI_API_KEY="AIzaSyBvE82VYWYZknp0g31a8WB6WvFQV_YbimE"
API_KEY = GEMINI_API_KEY
genai.configure(api_key=API_KEY)
# Initialize the Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')
# client = genai.Client(api_key=GEMINI_API_KEY)
prompt="hi"
# response = client.chat.completions.create(
#             model="gemini-2.0-flash",
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.7
#         )
chat=model.start_chat()
response = chat.send_message(
            
    prompt,
    generation_config={
        "temperature": 0.6

    })
response = chat.send_message(prompt)
llm_message = response.text.strip()



print(f"\nLLM: {llm_message}")


