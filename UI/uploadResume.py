import streamlit as st
import tempfile
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from nodes.resume_parser import parse_resume
from nodes.Interview_Preparation import prepare_interview_context
from utils.state_schema import BaseState
from InterviewPage import run_interview

def upload_resume_and_job_description():
    st.title("📄 Upload Resume & Job Description")

    resume_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
    job_description = st.text_area("Paste the Job Description Here", height=200)

    if resume_file and job_description:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(resume_file.read())
            resume_path = tmp.name

        initial_state :BaseState= {
            "resume": resume_path,
            "job_description": job_description,
            "stage": "start"
        }

        state = parse_resume(initial_state)
        if state["stage"] == "error":
            st.error(f"❌ Resume parsing failed: {state.get('error')}")
            return False

        state = prepare_interview_context(state)
        if state["stage"] == "error":
            st.error(f"❌ Interview context preparation failed: {state.get('error')}")
            return False

        # Save state globally
        st.session_state.interview_state = state
        st.success("✅ Resume parsed and interview context prepared successfully!")

        # ✅✅✅ PLACE THE VISUALIZATION HERE ✅✅✅
        st.header("📋 Candidate Profile Overview")

        # Summary
        st.subheader("🧠 Summary")
        st.info(state.get("summary", "No summary available."))

        # Extracted Resume Data
        extracted = state.get("extracted_data", {})
        if extracted:
            with st.expander("📄 Resume Highlights", expanded=True):
                st.markdown(f"**👤 Name:** {extracted.get('full_name', 'N/A')}")
                st.markdown(f"**📧 Email:** {extracted.get('email', 'N/A')}")
                st.markdown(f"**📞 Phone:** {extracted.get('phone', 'N/A')}")
                st.markdown(f"**🔗 LinkedIn:** {extracted.get('linkedin', 'N/A')}")
                st.markdown(f"**🛠️ Skills:** {', '.join(extracted.get('skills', []))}")
                st.markdown(f"**💼 Experience:** {extracted.get('experience', 'N/A')}")
                st.markdown(f"**🎓 Education:** {extracted.get('education', 'N/A')}")

        # Compatibility Check
        st.subheader("✅ Compatibility with Job")
        st.success(state.get("compatibility_check", "No compatibility analysis available."))

        # Suggested Interview Questions
        questions = state.get("interview_questions", [])
        if questions:
            with st.expander("🗣️ Suggested Interview Questions", expanded=False):
                for idx, q in enumerate(questions, 1):
                    st.markdown(f"**Q{idx}.** {q}")

        return True  # Everything succeeded

    return False  # Do nothing if inputs are missing
