from nodes.resume_parser import parse_resume
def chatbot_main(resume: str, job_description: str):
    # Initial state
    initial_state = {
        "resume": resume,
        "job_description": job_description,
        "stage": "start"
    }

    # Parse resume
    state = parse_resume(initial_state)
    if state["stage"] == "error":
        print("Error during resume parsing:", state.get("error"))
    #     return

    # # Conduct interview
    # state = interviewer_node(state)
    # if state["stage"] == "error":
    #     print("Error during interview process:", state.get("error"))
    #     return

    # # Generate feedback
    # state = feedback_node(state)
    # if state["stage"] == "error":
    #     print("Error during feedback generation:", state.get("error"))
    #     return

    # # Final Output
    # print("\nInterview Complete!")
    # print("Feedback:")
    # print(state["feedback"])


if __name__ == "__main__":
    resume = "/workspaces/Capstone_project-/data/resumeSample.pdf"
    job_description = "Senior Software Engineer with expertise in Python and AI."

    chatbot_main(resume, job_description)