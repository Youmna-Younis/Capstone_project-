mport sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ..nodes.resume_parser import parse_resume
from langgraph.graph import StateGraph, START, END
from ..utils.state_schema import ResumeParsingState

def test_parse_resume():
    initial_state = {
        "resume": "/workspaces/Capstone_project-/data/resumeSample.pdf",  
        "job_description": "Looking for a Python developer with expertise in Machine Learning and Data Analysis."
    }

    graph = StateGraph(ResumeParsingState)

    # Add the resume parsing node
    graph.add_node("ParseResume", parse_resume)

    # Set the graph flow: START → ParseResume → END
    graph.add_edge(START, "ParseResume")
    graph.add_edge("ParseResume", END)

    # Compile and return the graph
    graph= graph.compile()
    output = graph.invoke(initial_state)

    print("Parsed Resume:", output)