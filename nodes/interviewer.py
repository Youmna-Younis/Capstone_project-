import os
import json
import logging

from utils.state_schema import InterviewState
from utils.state_schema  import InterviewPreparationState

from utils.gemini_utils import Generate_response
from utils.evaluation_state import*



# ---------- System-Level Interview Handler ----------
def interview_chat_handler(prompt, conversation_history):
    config = {"temperature": 0.7}
    full_prompt = f"""
    {prompt}

    Here is the conversation so far:
    {json.dumps(conversation_history, indent=2)}

    Generate the next question or response for the candidate.
    If the interview is complete, respond with \"END\".
    """
    return Generate_response(full_prompt, config)

def conduct_interview(state: InterviewPreparationState) -> InterviewState:
    llm_context = state.get("llm_context", "")
    conversation_history = []
    Questions =[]
    Candidate_Response=[]
    responses=[]

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
        # chat=model.start_chat()   
        # # response = chat.send_message(
        # #     messages=[{"role": "user", "content": prompt}],
        # #     temperature=0.7
        # # )

        # # llm_message = response.choices[0].message.content.strip()

        # # if llm_message == "END":
        # #     break

        # # # Display the LLM's message
        # # print(f"\nLLM: {llm_message}")
        # response = chat.send_message(            
        #                            prompt,
        #                     generation_config={
        #                        "temperature": 0.6

        #                                         })
        # response = chat.send_message(prompt)
        config={ "temperature":0.7}
        llm_message=Generate_response(prompt,config)
        if llm_message == "END":
            break

        # Display the LLM's message
        print(f"\nLLM: {llm_message}")
        # Collect the user's response
        user_response = input("Candidate's Response: ").strip()
        Questions.append(llm_message)
        Candidate_Response.append(user_response)
        responses.append({"question": llm_message, "answer": user_response})

        # conversation_history.append({"role": "llm", "message": llm_message})
        # conversation_history.append({"role": "user", "message": user_response})

        return {
        **state,
        "Candidate_Response":Candidate_Response,
        "Questions":Questions,
        "responses":responses,
        # "conversation_history": conversation_history,
        "stage": "ready_for_evaluation"
    }
def follow_up_prompt(state:EvaluationState):
                            score=state["evaluation"]["score"]
                            feedback_summary=state["evaluation"]["summary"]

                            if score < 0.4:
                                        follow_up_prompt = f"""
                                                 The candidate struggled in the last response.

                                                   Weakness: {feedback_summary}
                                                    Ask a simple, clarification question to better understand their ability in this area.
                                                                               """
                            elif score > 0.8:
                                                 follow_up_prompt = f"""
                                               The candidate showed strong capability in the last response.

                                                Strength: {feedback_summary}

                                              Ask a deeper follow-up or a question that builds on this strength.
                                                      """
                            else:
                                                   follow_up_prompt = "Ask a new behavioral question."
                            return follow_up_prompt                       