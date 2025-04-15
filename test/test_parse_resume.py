from nodes.resume_parser import parse_resume
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ..nodes.resume_parser import parse_resume

def test_parse_resume():
    initial_state = {
        "resume": "/workspaces/Capstone_project-/data/resumeSample.pdf",  
        "job_description": "Looking for a Python developer with expertise in Machine Learning and Data Analysis."
    }

    final_state = parse_resume(initial_state)
    parsed_resume = final_state.get("parsed_resume")

    assert parsed_resume is not None
    assert "skills" in parsed_resume
    assert "experience" in parsed_resume
    print("Parsed Resume:", parsed_resume)