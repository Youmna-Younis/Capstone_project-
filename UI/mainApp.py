import streamlit as st
from uploadResume import upload_resume_and_job_description
from utils.state_schema import *
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from InterviewPage import run_interview  
# from interview_logic import run_interview  # Placeholder if you have this function
from FeedbackPage import Get_Report
if "InterviewState" not in st.session_state:
    st.session_state.InterviewState = {
        "resume": None,
        "job_description": None,
        "stage": "start",
        "evaluation": {}
    }
# Page setup
st.set_page_config(page_title="Smart HR Assistant", layout="centered")

# Sidebar navigation
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135789.png", width=80)
st.sidebar.title("Smart HR Assistant")
page = st.sidebar.radio("Navigate", [
    "🏠 Home", 
    "📄 Upload Resume & Job Description", 
    "💬 Start Interview with Sara", 
    "📊 Feedback Report"
])

# Page 1: Home
if page == "🏠 Home":
    st.title("Welcome to Smart HR Assistant 🎯")
    st.markdown("""
    **Your gateway to landing your dream job!**

    🚀 Here's how it works:
    - Upload your **resume** and a **job description** for your dream role.
    - Our AI interviewer **Sara** will conduct a professional, tailored interview.
    - Once you're done, get a **detailed feedback report** to improve and shine in real interviews!
    """)
    st.image(
           "Assets/img.png",
    caption="Sara - Your Personal AI Interviewer",
)

# Page 2: Upload Resume & JD
elif page == "📄 Upload Resume & Job Description":
    st.title("Upload Documents 📤")
    st.markdown("Please upload your resume and the job description of the position you're targeting.")
    
    success = upload_resume_and_job_description()
    if success:
        st.success("Files uploaded successfully.")
        st.info("You're all set! Proceed to the interview page to meet Sara.")

# Page 3: Start Interview
elif page == "💬 Start Interview with Sara":
             # Initialize interview flag if not set
            if "interview_in_progress" not in st.session_state:
                 st.session_state.interview_in_progress = False

                              # Show Start Interview button if not started
            if not st.session_state.interview_in_progress:
                                        if st.button("🎙️ Start Interview"):
                                              st.session_state.interview_in_progress = True
                                              st.rerun()
                                        else:
                                         st.info("Click the button above to begin the interview.")
            else:
                       run_interview()  # This now runs continuously across reruns
# Page 4: Feedback Report
elif page == "📊 Feedback Report":
    st.title("Your Feedback Report 🧾")
    st.markdown("""
    After your interview, this page shows:
    - ✅ Evaluation Summary
    - 📊 Strengths & Improvement Areas
    - 🎯 Personalized Interview Tips
    """)
    interview_state = st.session_state.interview_manager.state
    # Check if interview is completed
    if "interview_manager" not in st.session_state or not st.session_state.get("finished"):
        st.warning("⚠️ Report not generated yet. Please complete the interview first.")
        st.stop()
    else:    
           Get_Report(st.session_state.interview_manager.state)
    # Placeholder - replace with actual report display
    st.warning("Report not generated yet. Complete the interview first.")
