import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from interview_logic import InterviewManager  # Ensure this has your refactored logic
from utils.state_schema import InterviewPreparationState

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

# --- Setup session state ---
if "interview_started" not in st.session_state:
    initial_state = InterviewPreparationState({
        "llm_context": candidate_info,
        "HR_instructions": HRINST,
    })
    st.session_state.interview_manager = InterviewManager(initial_state)
    st.session_state.conversation_history = []
    st.session_state.welcome_shown = False
    st.session_state.follow_up = ""
    st.session_state.finished = False

# --- UI Header ---
st.set_page_config(page_title="AI HR Interviewer", layout="centered")
st.title("🤖 AI-Powered Interview Bot")
st.markdown("Sara (HR Bot) will guide you through a professional interview experience. Type `q` to quit.")

# --- Display initial welcome message once ---
if not st.session_state.welcome_shown:
    with st.chat_message("interviewer"):
        st.markdown("👋 Hello! I'm Sara, your HR interviewer today. Let's begin.")

    st.session_state.welcome_shown = True


# --- Display past conversation ---
for msg in st.session_state.interview_manager.state["conversation_history"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        

# --- Handle user input ---
if not st.session_state.finished:
    prompt = st.chat_input("Your response...")

    if prompt:
        if prompt.strip().lower() == "q":
            st.session_state.finished = True
            with st.chat_message("interviewer"):
                st.markdown("✅ Thank you for your time. The interview is now complete.")
        else:
            # Add user response
            st.chat_message("candidate").markdown(prompt)
            im = st.session_state.interview_manager
            im.state["candidate_responses"].append(prompt)
            im.state["conversation_history"].append({"role": "candidate", "content": prompt})

            # Evaluate and follow-up
            follow_up_prompt = im._evaluate_and_generate_instruction(prompt)
            st.session_state.follow_up = follow_up_prompt

            # Generate LLM next question
            GeneratedPrompt = im._generate_prompt(prompt)  # Generate prompt with follow-up instruction
            llm_response=im.generate_llm_response(GeneratedPrompt) 
            im.state["questions"].append(llm_response)
            im.state["conversation_history"].append({"role": "interviewer", "content": llm_response})
            
            # Show interviewer response
            with st.chat_message("interviewer"):
                st.markdown(llm_response)
