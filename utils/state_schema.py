# from typing import TypedDict, List

# class HRState(TypedDict):
#     """
#     State schema for the HR Assistant workflow.
#     """
#     resume: str  # Path to the candidate's resume
#     job_description: str  # Job description for compatibility checks
#     parsed_resume: dict  # Parsed resume data (output from resume parser)
#     responses: List[str]  # Candidate's interview responses
#     evaluation_results: dict  # Evaluation results (output from evaluator)

from typing_extensions import TypedDict
from typing import Optional, List, Dict
from typing import Dict, List, Optional, TypedDict

class BaseState(TypedDict):
    resume: str
    job_description: str
    resume_id: Optional[str]
    stage: Optional[str]
    error: Optional[str]
    details: Optional[str]

class ResumeParsingState(BaseState):
    extracted_data: Dict[str, str]
    compatibility_check: Optional[str]
    summary: Optional[str]
    interview_questions: List[str]

class InterviewPreparationState(ResumeParsingState):
    llm_context: Optional[str]  # Context provided to the LLM for conducting the interview

class InterviewState(InterviewPreparationState):
   # conversation_history: List[Dict[str, str]]  # Tracks the conversation as {"role": "user/llm", "message": "text"}
    Questions:List[str]
    Candidate_Response:List[str]

class FeedbackState(InterviewState):
    evaluation: Optional[Dict[str, str]]  # Stores evaluation results