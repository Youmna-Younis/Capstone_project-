import os
import json
import google.generativeai as genai
import logging

from utils.state_schema import InterviewState
from utils.state_schema  import InterviewPreparationState

from utils.gemini_utils import model
def conduct_interview(state: InterviewPreparationState) -> InterviewState:
    llm_context = state.get("llm_context", "")
    conversation_history = []
    Questions =[]
    Candidate_Response=[]

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
        chat=model.start_chat()   
        # response = chat.send_message(
        #     messages=[{"role": "user", "content": prompt}],
        #     temperature=0.7
        # )

        # llm_message = response.choices[0].message.content.strip()

        # if llm_message == "END":
        #     break

        # # Display the LLM's message
        # print(f"\nLLM: {llm_message}")
        response = chat.send_message(            
                                   prompt,
                            generation_config={
                               "temperature": 0.6

                                                })
        response = chat.send_message(prompt)
        llm_message = response.text.strip()

        # Collect the user's response
        user_response = input("Candidate's Response: ").strip()
        Questions.append(llm_message)
        Candidate_Response.append(user_response)
        # conversation_history.append({"role": "llm", "message": llm_message})
        # conversation_history.append({"role": "user", "message": user_response})

        return {
        **state,
        "Candidate_Response":Candidate_Response,
        "Questions":Questions,
        # "conversation_history": conversation_history,
        "stage": "ready_for_evaluation"
    }