import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from nodes.feedback_generator import generate_interview_report

def Get_Report( interview_state):
                   report_text = generate_interview_report(interview_state)

                   st.subheader("📋 Full Report")
                   st.text_area("Report", report_text, height=500)
                   st.download_button(
              label="📥 Download as .txt",
              data=report_text,
              file_name="interview_report.txt",
              mime="text/plain"
                         )
