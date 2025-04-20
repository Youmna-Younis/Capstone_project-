# interview_ui.py
import streamlit as st
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from interview_logic import InterviewManager
from utils.state_schema import InterviewPreparationState


def run_interview():
    #st.set_page_config(page_title="Interview with Sara", layout="centered")
    st.title("💬 Interview with Sara – Your AI HR Bot")

    parsed_state = st.session_state.get("interview_state", {})

    if not parsed_state or parsed_state.get("stage") != "ready_for_interview":
        st.warning("Please upload and parse your resume first on the previous page.")
        return 

    # Build dynamic candidate context
    extracted = parsed_state.get("extracted_data", {})
    job_description = parsed_state.get("job_description", "N/A")

    candidate_info = f"""
    Candidate Info:
    - Name: {extracted.get('full_name', 'Unknown')}
    - Role Applied: {job_description}
    - Skills: {', '.join(extracted.get('skills', []))}
    - Experience: {extracted.get('experience', 'N/A')}
    """

    HRINST = """
    You are Sara, a professional HR interviewer bot. Your task is to assess the candidate’s fit for the job
    by asking smart, professional, and engaging questions based on their background.
    Respond with empathy and professionalism.
    """

    # Initialize once
    if "interview_started" not in st.session_state:
        initial_state = InterviewPreparationState({
            "llm_context": candidate_info,
            "HR_instructions": HRINST,
        })
        st.session_state.interview_manager = InterviewManager(initial_state)
        st.session_state.interview_started = True
        st.session_state.welcome_shown = False
        st.session_state.finished = False
        st.session_state.follow_up = ""
        st.session_state.conversation = []
    # # Button to start the interview
    # start_clicked = st.button("🎙️ Start Interview")

    # # Set flag once and persist
    # if start_clicked:
    #     st.session_state.interview_started = True
    #     st.experimental_rerun()
    # else:
    #     st.info("Click the button above when you're ready to begin your interview.")
        
    # Initialize interview state    
    # Control start
    if not st.session_state.welcome_shown:
            with st.chat_message("interviewer"):
               st.markdown("👋 Hello! I'm Sara, your HR interviewer today. Let's begin.")
    
                  # ➕ Sara initiates the first question immediately
               first_question = st.session_state.interview_manager.generate_llm_response(
               st.session_state.interview_manager._generate_prompt("")
                                             )
    
               st.session_state.interview_manager.state["questions"].append(first_question)
               st.session_state.interview_manager.state["conversation_history"].append({
               "role": "interviewer", "content": first_question
                       })
               st.session_state.conversation.append({
                          "role": "interviewer", "content": first_question
                                        })
    
               st.session_state.welcome_shown = True
               st.experimental_rerun()


    # # Show welcome once
    # if not st.session_state.welcome_shown:
    #     with st.chat_message("interviewer"):
    #         st.markdown("👋 Hello! I'm Sara, your HR interviewer today. Let's begin.")
    #     st.session_state.welcome_shown = True

    # Show history
    for msg in st.session_state.interview_manager.state["conversation_history"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Handle input
    if not st.session_state.finished:
        prompt = st.chat_input("Your response...")

        if prompt:
            if prompt.strip().lower() == "q":
                st.session_state.finished = True
                with st.chat_message("interviewer"):
                    st.markdown("✅ Thank you. The interview is now complete.")
            else:
                im = st.session_state.interview_manager

                st.chat_message("candidate").markdown(prompt)
                im.state["candidate_responses"].append(prompt)
                im.state["conversation_history"].append({"role": "candidate", "content": prompt})
                st.session_state.conversation.append({"role": "candidate", "content": prompt})

                with st.spinner("Sara is thinking..."):
                    follow_up_prompt = im._evaluate_and_generate_instruction(prompt)
                    st.session_state.follow_up = follow_up_prompt

                    generated_prompt = im._generate_prompt(prompt)
                    llm_response = im.generate_llm_response(generated_prompt)

                im.state["questions"].append(llm_response)
                im.state["conversation_history"].append({"role": "interviewer", "content": llm_response})
                st.session_state.conversation.append({"role": "interviewer", "content": llm_response})

                with st.chat_message("interviewer"):
                    st.markdown(llm_response)

    # Save for feedback
    #st.session_state.interview_state["conversation"] = st.session_state.conversation



def run_interview2():
    st.set_page_config(page_title="Smart HR Assistant", layout="centered")

    #st.set_page_config(page_title="Interview with Sara", layout="centered")
    st.title("💬 Interview with Sara – Your AI HR Bot")
    # HR instructions & candidate info can be loaded from file or user input (static for now)
    HRINST = """
                      You are Sara, a professional HR interviewer bot. Your task is to assess the candidate’s fit for the job
by asking smart, professional, and engaging questions based on their background.
Respond with empathy and professionalism.
"""

    candidate_info = """
Candidate Info:
- Name: John Doe
- Role Applied: Backend Engineer
- Skills: Python, Django, REST APIs, PostgreSQL
- Experience: 4 years in backend development
"""


    # Initialize once
    if "interview_started" not in st.session_state:
        initial_state = InterviewPreparationState({
            "llm_context": candidate_info,
            "HR_instructions": HRINST,
        })
        st.session_state.interview_manager = InterviewManager(initial_state)
        st.session_state.interview_started = True
        st.session_state.welcome_shown = False
        st.session_state.finished = False
        st.session_state.follow_up = ""
        st.session_state.conversation = []
    # # Button to start the interview
    # start_clicked = st.button("🎙️ Start Interview")

    # # Set flag once and persist
    # if start_clicked:
    #     st.session_state.interview_started = True
    #     st.experimental_rerun()
    # else:
    #     st.info("Click the button above when you're ready to begin your interview.")
        
    # Initialize interview state    
    # Control start
    if not st.session_state.welcome_shown:
            with st.chat_message("interviewer"):
               st.markdown("👋 Hello! I'm Sara, your HR interviewer today. Let's begin.")
    
                  # ➕ Sara initiates the first question immediately
               first_question = st.session_state.interview_manager.generate_llm_response(
               st.session_state.interview_manager._generate_prompt("")
                                             )
    
               st.session_state.interview_manager.state["questions"].append(first_question)
               st.session_state.interview_manager.state["conversation_history"].append({
               "role": "interviewer", "content": first_question
                       })
               st.session_state.conversation.append({
                          "role": "interviewer", "content": first_question
                                        })
    
               st.session_state.welcome_shown = True
               st.experimental_rerun()


    # # Show welcome once
    # if not st.session_state.welcome_shown:
    #     with st.chat_message("interviewer"):
    #         st.markdown("👋 Hello! I'm Sara, your HR interviewer today. Let's begin.")
    #     st.session_state.welcome_shown = True

    # Show history
    for msg in st.session_state.interview_manager.state["conversation_history"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Handle input
    if not st.session_state.finished:
        prompt = st.chat_input("Your response...")

        if prompt:
            if prompt.strip().lower() == "q":
                st.session_state.finished = True
                with st.chat_message("interviewer"):
                    st.markdown("✅ Thank you. The interview is now complete.")
            else:
                im = st.session_state.interview_manager

                st.chat_message("candidate").markdown(prompt)
                im.state["candidate_responses"].append(prompt)
                im.state["conversation_history"].append({"role": "candidate", "content": prompt})
                st.session_state.conversation.append({"role": "candidate", "content": prompt})

                with st.spinner("Sara is thinking..."):
                    follow_up_prompt = im._evaluate_and_generate_instruction(prompt)
                    st.session_state.follow_up = follow_up_prompt

                    generated_prompt = im._generate_prompt(prompt)
                    llm_response = im.generate_llm_response(generated_prompt)

                im.state["questions"].append(llm_response)
                im.state["conversation_history"].append({"role": "interviewer", "content": llm_response})
                st.session_state.conversation.append({"role": "interviewer", "content": llm_response})

                with st.chat_message("interviewer"):
                    st.markdown(llm_response)

    # Save for feedback
    #st.session_state.interview_state["conversation"] = st.session_state.conversation

# if __name__ == "__main__":
#     run_interview2()
# # run_interview2()
# # run_interview()
