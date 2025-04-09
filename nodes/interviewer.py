
from utils.voice_io import speak, listen

def run_interview(state):
    questions = state["questions"]
    responses = []
    speak("Let's begin the voice interview.")

    for question in questions:
        speak(question)
        response = listen()
        responses.append({"question": question, "answer": response})
    
    return {"responses": responses}
