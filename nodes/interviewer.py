import os
import json
import google.generativeai as genai
import logging

from utils.state_schema import InterviewState
from utils.gemini_utils import InterviewPreparationState

def conduct_interview(state: InterviewPreparationState) -> InterviewState:
    llm_context = state.get("llm_context", "")
    conversation_history = []

    print("\nStarting Interview Process...")
    while True:
        # Generate the next question using the LLM
        prompt = f"""
        {llm_context}

        Here is the conversation so far:
        {json.dumps(conversation_history, indent=2)}

        Generate the next question or response for the candidate.
        If the interview is complete, respond with "END".
        """

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        llm_message = response.choices[0].message.content.strip()

        if llm_message == "END":
            break

        # Display the LLM's message
        print(f"\nLLM: {llm_message}")

        # Collect the user's response
        user_response = input("Candidate's Response: ").strip()
        conversation_history.append({"role": "llm", "message": llm_message})
        conversation_history.append({"role": "user", "message": user_response})

    return {
        **state,
        "conversation_history": conversation_history,
        "stage": "ready_for_evaluation"
    }