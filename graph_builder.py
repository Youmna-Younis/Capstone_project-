
from langgraph.graph import StateGraph
from nodes.resume_parser import parse_resume
from nodes.interviewer import run_interview
from nodes.evaluator import evaluate_responses

def build_graph():
    workflow = StateGraph()
    
    workflow.add_node("parse_resume", parse_resume)
    workflow.add_node("run_interview", run_interview)
    workflow.add_node("evaluate_responses", evaluate_responses)
    
    workflow.set_entry_point("parse_resume")
    workflow.add_edge("parse_resume", "run_interview")
    workflow.add_edge("run_interview", "evaluate_responses")
    
    workflow.set_finish_point("evaluate_responses")

    return workflow.compile()
