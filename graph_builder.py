from langgraph.graph import StateGraph
from nodes.resume_parser import parse_resume
from nodes.interviewer import run_interview
from nodes.evaluator import evaluate_responses
from typing import TypedDict, List
from utils.state_schema import HRState
def build_graph():
    # Initialize the StateGraph with the state schema
    workflow = StateGraph(HRState)

    # Add nodes
    workflow.add_node("parse_resume", parse_resume)
    workflow.add_node("run_interview", run_interview)
    workflow.add_node("evaluate_responses", evaluate_responses)

    # Set entry point and transitions
    workflow.set_entry_point("parse_resume")
    workflow.add_edge("parse_resume", "run_interview")
    workflow.add_edge("run_interview", "evaluate_responses")

    # Set finish point
    workflow.set_finish_point("evaluate_responses")

    return workflow.compile()