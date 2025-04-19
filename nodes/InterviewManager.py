import os
import json
import logging
from typing import Dict, List

from utils.state_schema import InterviewState, InterviewPreparationState, EvaluationState
from utils.gemini_utils import Generate_response
from nodes.evaluator import evaluate_responses
from utils.evaluation_state import EvaluationState
logger = logging.getLogger(__name__)

class InterviewManager:
    """Orchestrates the interview process with dynamic follow-up questions"""
    
    def __init__(self, initial_state: InterviewPreparationState):
        self.state = {
            **initial_state,
            "conversation_history": [],
            "questions": [],
            "candidate_responses": [],
            "evaluations": [EvaluationState]
        }
        
    def _generate_llm_prompt(self, follow_up_instruction: str = "") -> str:
        """Build context-aware prompt for LLM"""
        base_context = self.state["llm_context"]
        history = json.dumps(self.state["conversation_history"], indent=2)
        
        return f"""
        {base_context}
        
        {follow_up_instruction}
        
        Conversation History:
        {history}
        
        Generate a relevant interview question or response.
        If the interview should end, respond with "END".
        """
    
    def _handle_evaluation(self, state) -> Dict:
        """Evaluate candidate response and generate follow-up instructions"""
        evaluation = evaluate_responses( self.state)
        self.state["evaluations"].append(evaluation)
        
        # Create temporary evaluation state for follow-up prompt
        #eval_state = EvaluationState({"evaluation": evaluation})
        return self._generate_follow_up_prompt(evaluation)
    
    def _generate_follow_up_prompt(self, eval_state: EvaluationState) -> str:
        """Generate context-aware follow-up prompt based on evaluation"""
        score = eval_state["evaluation"]["score"]
        feedback = eval_state["evaluation"]["summary"]
        
        if score < 0.4:
            return f"""
            Candidate struggled with last question. Focus on clarifying:
            Weakness: {feedback}
            Ask a clarifying question to better understand their knowledge.
            """
        elif score > 0.8:
            return f"""
            Candidate demonstrated strong knowledge. Expand on:
            Strength: {feedback}
            Ask an advanced follow-up to explore deeper understanding.
            """
        return "Continue with a new relevant question."
    
    def conduct_interview(self) -> InterviewState:
        """Main interview loop with dynamic follow-up handling"""
        print("\nStarting AI-Powered Interview...")
        follow_up = ""
        
        for _ in range(2):
            # Generate context-aware question
            prompt = self._generate_llm_prompt(follow_up)
            llm_config = {"temperature": 0.7}
            
            try:
                llm_response = Generate_response(prompt, llm_config).strip()
            except Exception as e:
                logger.error(f"LLM Error: {str(e)}")
                llm_response = "END"
            
            if llm_response == "END":
                print("\nInterview completed successfully!")
                break
            
            # Process LLM question
            print(f"\nInterviewer: {llm_response}")
            user_response = input("Candidate: ").strip()
            
            # Update conversation state
            self.state["questions"].append(llm_response)
            self.state["candidate_responses"].append(user_response)
            self.state["conversation_history"].extend([
                {"role": "interviewer", "content": llm_response},
                {"role": "candidate", "content": user_response}
            ])
            
            # Generate follow-up based on evaluation
            follow_up = self._handle_evaluation(user_response)
        
        return {
            **self.state,
            "stage": "ready_for_evaluation",
            "questions":self.state["questions"],
            "candidate_responses":self.state["candidate_responses"],

        }
    
    # def _generate_summary(self) -> Dict:
    #     """Create final interview summary"""
    #     return {
    #         "total_questions": len(self.state["questions"]),
    #         "average_score": sum(e["score"] for e in self.state["evaluations"])/len(self.state["evaluations"]),
    #         "strengths": [e["summary"] for e in self.state["evaluations"] if e["score"] > 0.7],
    #         "weaknesses": [e["summary"] for e in self.state["evaluations"] if e["score"] < 0.4]
    #     }

