import os
import json
import logging
from typing import Dict, List

from utils.state_schema import InterviewState, InterviewPreparationState, EvaluationState
from utils.gemini_utils import Generate_response
from nodes.evaluator import evaluate_responses
from utils.evaluation_state import EvaluationState

logger = logging.getLogger(__name__)
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Global HR instructions
HRINST = """
You are an AI interviewer named Sara. Be professional, supportive, and mimic a natural human tone.
Avoid repetition. Build on prior answers. Do not reintroduce candidate context each time.
"""

class InterviewManager:
    def __init__(self, initial_state: InterviewPreparationState):
        self.state = {
            **initial_state,
            "conversation_history": [],
            "questions": [],
            "candidate_responses": [],
            "evaluations": []
        }

    def get_welcome_message(self) -> str:
        return """
Hi, I'm Sara, your AI interviewer today. Let's get started with a few questions to understand your experience.
Feel free to answer naturally. Ready?
"""

    def _generate_prompt(self, follow_up_instruction: str = "") -> str:
        """Assembles the prompt for the LLM based on current state"""
        history = json.dumps(self.state["conversation_history"], indent=2)

        prompt = f"""
        {HRINST}

        Candidate Info:
        {self.state['llm_context']}

        {follow_up_instruction}

        Conversation History:
        {history}

        Generate a relevant interview question or response.
        If the interview should end, respond with "END".
        """
        return prompt

    def _evaluate_and_generate_instruction(self, response: str) -> str:
        """Evaluates response and returns a follow-up instruction"""
        self.state["candidate_responses"].append(response)
        evaluation = evaluate_responses(self.state)
        self.state["evaluations"].append(evaluation)

        score = evaluation["evaluation"]["score"]
        feedback = evaluation["evaluation"]["summary"]

        if score < 0.4:
            return f"Candidate struggled. Clarify: Weakness: {feedback}\nAsk a simpler or probing question."
        elif score > 0.8:
            return f"Candidate performed well:Strength: {feedback}\nAsk a deeper or advanced follow-up."
        else:
            return "Continue with a new relevant question."

    def generate_llm_response(self, prompt: str) -> str:
        """Isolated LLM response handler"""
        llm_config = {"temperature": 0.7}
        try:
            return Generate_response(prompt, llm_config).strip()
        except Exception as e:
            logger.error(f"LLM Error: {str(e)}")
            return "END"

    def conduct_interview(self) -> InterviewState:
        print("\nStarting AI-Powered Interview...")
        print(f"\nInterviewer: {self.get_welcome_message().strip()}")

        follow_up_instruction = ""

        while True:
            prompt = self._generate_prompt(follow_up_instruction)
            llm_question = self.generate_llm_response(prompt)

            if llm_question == "END":
                print("\nInterview completed successfully!")
                break

            print(f"\nInterviewer: {llm_question}")
            user_response = input("Candidate: ").strip()

            self.state["questions"].append(llm_question)
            self.state["conversation_history"].extend([
                {"role": "interviewer", "content": llm_question},
                {"role": "candidate", "content": user_response}
            ])

            follow_up_instruction = self._evaluate_and_generate_instruction(user_response)

        return {
            **self.state,
            "stage": "ready_for_evaluation",
            "questions": self.state["questions"],
            "candidate_responses": self.state["candidate_responses"]
        }
