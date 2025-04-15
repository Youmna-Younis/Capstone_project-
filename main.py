from graph_builder import build_graph

if __name__ == "__main__":
    # Build the workflow
    workflow = build_graph()

    # Define the initial state
    initial_state = {
        "resume": "/workspaces/Capstone_project-/data/candidate_resume.txt",  
        "job_description": "Looking for a Python developer with expertise in Machine Learning and Data Analysis."
    }

    # Run the workflow using .invoke()
    final_state = workflow.invoke(initial_state)

    # Print the results
    print("Candidate Responses:", final_state.get("responses", []))
    print("Evaluation Results:", final_state.get("evaluation_results", {}))