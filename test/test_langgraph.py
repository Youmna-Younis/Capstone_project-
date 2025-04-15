from langgraph.graph import Graph

# Define the nodes
def start_node(state):
    print("Starting the workflow.")
    state["step"] = "started"
    return state

def middle_node(state):
    print("Processing data.")
    state["step"] = "processed"
    return state

def end_node(state):
    print("Workflow completed.")
    state["step"] = "completed"
    return state

# Build the graph
def build_graph():
    workflow = Graph()

    # Add nodes
    workflow.add_node("start", start_node)
    workflow.add_node("middle", middle_node)
    workflow.add_node("end", end_node)

    # Set entry point and transitions
    workflow.set_entry_point("start")
    workflow.add_edge("start", "middle")
    workflow.add_edge("middle", "end")

    # Set finish point
    workflow.set_finish_point("end")

    return workflow.compile()

# Run the test
if __name__ == "__main__":
    print("Testing LangGraph...")
    
    # Build the workflow
    graph = build_graph()

    # Initialize the state
    initial_state = {}

    # Run the workflow
    final_state = graph.invoke(initial_state)

    # Print the final state
    print("Final State:", final_state)