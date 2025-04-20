Here’s the updated README.md with a **User Manual** section added, including instructions for ending the interview by typing `q`:

```markdown
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

### **Agents (Nodes) in LangGraph**

1. **Resume Parsing Agent** (`resume_parser.py`):
   - Extracts key details (skills, education, experience) from uploaded resumes.
   - Uses **Document Understanding** to analyze resumes in PDF format.
   - Outputs structured data for compatibility checks and interview preparation.

2. **Job Compatibility Checker Agent** (`compatibility_checker.py`):
   - Matches the candidate's profile with the job description.
   - Uses **Grounding** to ensure the generated questions are relevant to the job role.
   - Provides a compatibility score and generates dynamic interview questions.

3. **Interview Preparation Agent** (`Interview_Preparation.py`):
   - Prepares the interview context by combining resume data, job compatibility results, and static/dynamic questions.
   - Creates a tailored context for the AI interviewer.

4. **AI-Powered Interview Agent** (`interviewer.py`):
   - Conducts a dynamic interview with "Sara," our conversational AI.
   - Uses **Controlled Generation** and **Few-Shot Prompting** to generate tailored questions based on the candidate's profile.
   - Maintains a conversation history for context-aware interactions.

5. **Response Evaluation Agent** (`evaluator.py`):
   - Evaluates candidate responses using **Gen AI Evaluation**.
   - Scores responses on a scale of 0.0 to 1.0 and provides detailed feedback.
   - Generates follow-up instructions based on the evaluation.

6. **Feedback Generation Agent** (`feedback_generator.py`):
   - Generates a detailed feedback report summarizing the candidate's performance.
   - Uses **Function Calling** to structure the report and highlight strengths, weaknesses, and overall impressions.

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
│   ├── resume_parser.py        # Resume Parsing Agent
│   ├── compatibility_checker.py # Job Compatibility Checker Agent
│   ├── Interview_Preparation.py # Interview Preparation Agent
│   ├── interviewer.py          # AI-Powered Interview Agent
│   ├── evaluator.py            # Response Evaluation Agent
│   ├── feedback_generator.py   # Feedback Generation Agent
├── utils/
│   ├── gemini_utils.py         # Utility functions for interacting with Google Gemini API
│   ├── state_schema.py         # Defines state schemas for the workflow
│   ├── summary_generator.py    # Generates summaries from extracted data
│   ├── data_extractor.py       # Extracts and parses data from resumes
├── data/
│   ├── candidate_resume.txt    # Sample resume data
├── requirements.txt            # Python dependencies
├── setup.py                    # Project setup configuration
├── .env                        # Environment variables (e.g., API keys)
├── README.md                   # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Google Gemini API Key (add it to the `.env` file)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/smart-hr-assistant.git
   cd smart-hr-assistant
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your Google API key to the `.env` file:
   ```plaintext
   GOOGLE_API_KEY="your-google-api-key"
   ```

4. Run the application:
   ```bash
   streamlit run UI/mainApp.py
   ```

---

## 📖 User Manual

### **1. Upload Resume & Job Description**
- Navigate to the **Upload Resume & Job Description** page.
- Upload your resume (PDF format) and paste the job description into the provided field.

### **2. Start the Interview**
- Go to the **Start Interview with Sara** page.
- The AI interviewer will ask dynamic questions based on your resume and job description.
- Type your responses in the input field.

### **3. End the Interview**
- When you want to end the interview, simply type `q` and press Enter.
- The system will stop the interview and proceed to generate a feedback report.

### **4. View Feedback Report**
- After the interview ends, navigate to the **Feedback Report** page.
- Review your strengths, weaknesses, and overall performance.

---

## 🧪 Testing

Run the following command to execute unit tests (if implemented):
```bash
pytest
```

---

## 🏆 Future Enhancements

- Add support for voice-based interviews.
- Integrate advanced memory for follow-up questions.
- Export interview sessions as PDF or JSON reports.
- Support for additional AI models like OpenAI GPT.

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

For questions or feedback, please reach out to us at `your-email@example.com`.

---

Enjoy using **Smart HR Assistant**! 🎉
```