from nodes.resume_parser import parse_resume
from nodes.Interview_Preparation import prepare_interview_context
from utils.state_schema import *
from nodes.interviewer import conduct_interview

# def chatbot_main(resume: str, job_description: str):
#     # Initial state
#     initial_state = {
#         "resume": resume,
#         "job_description": job_description,
#         "stage": "start"
#     }

#     # Parse resume
#     state = parse_resume(initial_state)
#     if state["stage"] == "error":
#         print("Error during resume parsing:", state.get("error"))
#         return
#         # Step 2: Prepare interview context
#     state = prepare_interview_context(state)
#     if state["stage"] == "error":
#         print("Error during interview preparation:", state.get("error"))
#         return

#     # # Conduct interview
#     # state = interviewer_node(state)
#     # if state["stage"] == "error":
#     #     print("Error during interview process:", state.get("error"))
#     #     return

#     # # Generate feedback
#     # state = feedback_node(state)
#     # if state["stage"] == "error":
#     #     print("Error during feedback generation:", state.get("error"))
#     #     return

#     # # Final Output
#     # print("\nInterview Complete!")
#     # print("Feedback:")
#     # print(state["feedback"])

def chatbot_main(resume: str, job_description: str):
    # Initial state
    initial_state: BaseState = {
        "resume": resume,
        "job_description": job_description,
        "stage": "start"
    }

    # Step 1: Parse the resume
    state = parse_resume(initial_state)
    if state["stage"] == "error":
        print("Error during resume parsing:", state.get("error"))
        return

    # Step 2: Prepare interview context
    state = prepare_interview_context(state)
    if state["stage"] == "error":
        print("Error during interview preparation:", state.get("error"))
        return

    # Step 3: Conduct the interview
    state = conduct_interview(state)
    if state["stage"] == "error":
        print("Error during interview process:", state.get("error"))
        return 
    print(f'canditat responsee : {state["Candidate_Response"]}')

    # # Step 4: Evaluate responses
    # state = evaluate_responses(state)
    # if state["stage"] == "error":
    #     print("Error during evaluation:", state.get("error"))
    #     return

    # # Final Output
    # print("\nInterview Complete!")
    # print("Evaluation:")
    # print(state["evaluation"])

if __name__ == "__main__":
    resume = "/workspaces/Capstone_project-/data/resumeSample.pdf"
    job_description = "Senior Software Engineer with expertise in Python and AI."

    chatbot_main(resume, job_description)
