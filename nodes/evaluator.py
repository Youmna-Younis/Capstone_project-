
def evaluate_responses(state):
    responses = state["responses"]
    summary = "Candidate responded confidently to all questions."
    return {
        "evaluation": {
            "summary": summary,
            "score": 8.5,
            "responses": responses
        }
    }
