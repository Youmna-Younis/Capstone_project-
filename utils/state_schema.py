from typing import TypedDict, List

class HRState(TypedDict):
    """
    State schema for the HR Assistant workflow.
    """
    resume: str  # Path to the candidate's resume
    job_description: str  # Job description for compatibility checks
    parsed_resume: dict  # Parsed resume data (output from resume parser)
    responses: List[str]  # Candidate's interview responses
    evaluation_results: dict  # Evaluation results (output from evaluator)