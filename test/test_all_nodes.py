from nodes.resume_parser import parse_resume
from nodes.interviewer import run_interview
from nodes.evaluator import evaluate_responses

# Step 1: Test parse_resume
initial_state = {
    "resume": "/workspaces/Capstone_project-/data/resumeSample.pdf",  
    "job_description": "Looking for a Python developer with expertise in Machine Learning and Data Analysis."
}
state = parse_resume(initial_state)
print("Parsed Resume:", state.get("parsed_resume"))

# Step 2: Test run_interview
state["responses"] = []  # Initialize an empty list for responses
state = run_interview(state)
print("Candidate Responses:", state.get("responses"))

# Step 3: Test evaluate_responses
state["evaluation_results"] = {}  # Initialize an empty dictionary for evaluation results
state = evaluate_responses(state)
print("Evaluation Results:", state.get("evaluation_results"))