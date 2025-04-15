from utils.voice_io import text_to_speech, speech_to_text
from utils.gemini_utils import generate_response
from utils.state_schema import HRState

def run_interview(state: HRState) -> HRState:
    """
    Conducts the interview process.
    """
    # Extract parsed resume data from the state
    parsed_resume = state.get("parsed_resume", {})
    compatibility_check = parsed_resume.get("compatibility_check", {})
    summary = parsed_resume.get("summary", "")
    interview_questions = parsed_resume.get("interview_questions", [])

    print(f"HR: Hi there! Welcome to the interview process. Let’s get started!")
    text_to_speech("Hi there! Welcome to the interview process. Let’s get started!")

    # Share the summary with the candidate
    print(f"HR: Based on your resume, here’s a summary of your profile: {summary}")
    text_to_speech(f"Based on your resume, here’s a summary of your profile: {summary}")

    # Share compatibility feedback
    compatibility_feedback = compatibility_check.get("feedback", "")
    if compatibility_feedback:
        print(f"HR: Our initial assessment shows: {compatibility_feedback}")
        text_to_speech(f"Our initial assessment shows: {compatibility_feedback}")

    # Store candidate responses
    candidate_responses = []

    # Ask predefined and dynamic questions
    for i, question in enumerate(interview_questions, 1):
        print(f"\nQuestion {i}:")
        response = ask_question(question)
        if response:
            print(f"Candidate: {response}")
            candidate_responses.append(response)

            # Generate a follow-up question
            follow_up = generate_follow_up(response)
            print(f"HR: {follow_up}")
            text_to_speech(follow_up)

    # Update the state with the candidate's responses
    state["responses"] = candidate_responses

    # Conclude the interview
    conclusion = ("Thank you for completing the interview. "
                  "We’ll review your responses and get back to you soon.")
    print(f"\nHR: {conclusion}")
    text_to_speech(conclusion)

    return state


def ask_question(question):
    """
    Asks a question and listens to the candidate's response.
    """
    print(f"HR: {question}")
    text_to_speech(question)  # Speak the question
    response = speech_to_text()  # Listen to the candidate's response
    if response:
        return response.strip()
    return None


def generate_follow_up(response):
    """
    Generates a follow-up response using Gemini.
    """
    prompt = f"The candidate said: '{response}'. Generate a relevant and engaging follow-up question or feedback."
    return generate_response(prompt)