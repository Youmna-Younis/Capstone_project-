import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nodes.interviewer import run_interview

# Mock the text_to_speech function
def mock_text_to_speech(text):
    print(f"Text-to-Speech: {text}")

# Override the actual text_to_speech function with the mock
def test_run_interview():
    # Define the initial state
    initial_state = {
        "parsed_resume": {
            "skills": ["Python", "Machine Learning"],
            "experience": "5 years",
            "education": "Bachelor's in Computer Science"
        },
        "candidate_responses": []
    }

    # Mock the text_to_speech function
    from utils.voice_io import text_to_speech
    original_text_to_speech = text_to_speech
    try:
        from utils.voice_io import text_to_speech
        text_to_speech = mock_text_to_speech

        # Run the interview
        final_state = run_interview(initial_state)

        # Assertions
        assert len(final_state.get("candidate_responses")) == 3
        assert "5 years of experience" in final_state["candidate_responses"][0]
        assert "problem-solving" in final_state["candidate_responses"][1]
        assert "grow my career" in final_state["candidate_responses"][2]
    finally:
        # Restore the original text_to_speech function
        text_to_speech = original_text_to_speech

if __name__ == "__main__":
    test_run_interview()