# 🧠 Smart HR Assistant – AI-Powered Mock Interviewer

**Smart HR Assistant** is an AI-powered platform designed to help job seekers land their dream jobs by simulating real-world interviews. This project is the **Capstone Project** for the **Gen AI Intensive Course**, where we applied cutting-edge Generative AI capabilities to build a system that provides personalized interview preparation. 

With just a resume and a job description, the system generates tailored interview questions, conducts a mock interview with "Sara" (our AI chatbot), and provides a detailed feedback report highlighting your strengths, weaknesses, and performance on each question.

---

## 🌟 Problem Statement

Job interviews can be intimidating, and many candidates struggle to prepare effectively. Traditional preparation methods often fail to provide personalized feedback or simulate the dynamic nature of real interviews. **Smart HR Assistant** solves this problem by offering:

- A **personalized mock interview experience** tailored to your resume and the job description.
- **Dynamic, AI-generated questions** that adapt to your responses.
- A **comprehensive feedback report** to help you identify areas for improvement and boost your confidence.

With **Smart HR Assistant**, you can practice interviews in a safe environment and gain the insights you need to excel in your next real-world interview.

---

## 🚀 Features

This project is built using **LangGraph**, where each feature is represented as an **Agent (Node)** in the graph. These agents work together to create a seamless interview preparation experience:

1. **Resume Parsing Agent**:
   - Extracts key details (skills, education, experience) from uploaded resumes.
   - Uses **Document Understanding** to analyze resumes in PDF format.

2. **Job Description Analysis Agent**:
   - Matches the candidate's profile with the job description.
   - Uses **Grounding** to ensure the generated questions are relevant to the job role.

3. **AI-Powered Interview Agent**:
   - Conducts a dynamic interview with "Sara," our conversational AI.
   - Uses **Controlled Generation** and **Few-Shot Prompting** to generate tailored questions based on the candidate's profile.

4. **Feedback Generation Agent**:
   - Evaluates candidate responses and generates a detailed feedback report.
   - Uses **Gen AI Evaluation** to assess responses and provide actionable insights.

5. **Follow-Up Question Agent**:
   - Dynamically generates follow-up questions based on the candidate's performance.
   - Uses **Function Calling** to adaptively create questions that probe deeper into strengths or clarify weaknesses.

---

## 🛠️ GenAI Capabilities Applied

This project leverages the following **Generative AI capabilities**:

- **Agents**: Each feature is implemented as an independent agent in the LangGraph framework.
- **Controlled Generation**: Ensures that interview questions and feedback are structured and relevant.
- **Few-Shot Prompting**: Provides context to the AI model for generating tailored questions.
- **Document Understanding**: Extracts and processes information from resumes and job descriptions.
- **Gen AI Evaluation**: Evaluates candidate responses to generate feedback.
- **Grounding**: Ensures that the AI-generated content aligns with the job description and candidate profile.
- **Long Context Window**: Handles extended conversations and maintains context throughout the interview process.

---

## 🖼️ How It Works (Visual Workflow)

1. **Upload Resume & Job Description**  
   ![Upload Resume](placeholder-upload-resume.png)  
   Upload your resume and paste the job description. The system analyzes your profile and prepares tailored questions.

2. **Start the Interview**  
   ![Start Interview](placeholder-start-interview.png)  
   Begin the mock interview with "Sara." Answer questions dynamically generated based on your resume and the job description.

3. **End the Interview & Generate Feedback**  
   ![Feedback Report](placeholder-feedback-report.png)  
   After completing the interview (press `q` to end), the system generates a feedback report showing your performance.

---

## 📂 Project Structure

```plaintext
/workspaces/Capstone_project-/
├── UI/
│   ├── mainApp.py              # Main entry point for the Streamlit app
│   ├── uploadResume.py         # Handles resume and job description uploads
│   ├── InterviewPage.py        # Conducts the interview with the AI interviewer
│   ├── FeedbackPage.py         # Generates and displays feedback reports
├── nodes/
│   ├── resume_parser.py        # Extracts data from resumes
│   ├── InterviewManager.py     # Manages the interview process
│   ├── [interviewer.py](http://_vscodecontentref_/1)          # Handles interview logic and follow-up questions
│   ├── feedback_generator.py   # Generates feedback for candidate responses
│   ├── evaluator.py            # Evaluates candidate responses
│   ├── Interview_Preparation.py # Prepares interview context
├── utils/
│   ├── gemini_utils.py         # Utility functions for interacting with Google Gemini API
│   ├── state_schema.py         # Defines state schemas for the workflow
│   ├── summary_generator.py    # Generates summaries from extracted data
│   ├── data_extractor.py       # Extracts and parses data from resumes
│   ├── compatibility_checker.py # Checks compatibility between resumes and job descriptions
├── data/
│   ├── candidate_resume.txt    # Sample resume data
├── [requirements.txt](http://_vscodecontentref_/2)            # Python dependencies
├── [setup.py](http://_vscodecontentref_/3)                    # Project setup configuration
├── .env                        # Environment variables (e.g., API keys)
├── [README.md](http://_vscodecontentref_/4)                   # Project documentation
## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Google Gemini API Key (add it to the `.env` file)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/smart-hr-assistant.git
   cd smart-hr-assistant

2. Install dependencies:
  ```bash
     pip install -r requirements.txt   cd smart-hr-assistant   

3. Add your Google API key to the .env file:
  ```bash
     GOOGLE_API_KEY="your-google-api-key"     

4. Run the application:
   ```bash
      streamlit run UI/mainApp.py
   