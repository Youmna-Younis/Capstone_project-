# 🧠 AI HR Assistant – Project Plan & Timeline (April 7–20)

## 📅 Timeline Overview

| Date Range       | Phase                           | Key Activities                                                                 | Expected Output / Deliverables                                   |
|------------------|----------------------------------|---------------------------------------------------------------------------------|------------------------------------------------------------------|
| **April 7**       | Research & Exploration          | - Conduct individual research on Gen AI in HR<br>- Study existing solutions and innovations<br>- Investigate technical approaches (e.g., agents, LLMs, prompt tuning) | Curated list of references, relevant tools, and potential use cases |
| **April 8**       | Ideation & Planning Workshop    | - Team meeting to consolidate research<br>- Define use case, input/output flows<br>- Determine project scope and boundaries<br>- Finalize technical architecture & tool stack | Clearly defined project scope document<br>High-level system design<br>Task assignments |
| **April 9–11**    | System Design & Initial Build   | - Set up development environment<br>- Implement core agents (e.g., resume parser, question generator)<br>- Begin building system logic | Functional agent prototypes<br>Basic working version of assistant logic |
| **April 12–13**   | Feature Integration & Testing   | - Integrate agents into a unified flow<br>- Implement user interaction logic (role/company input)<br>- Conduct unit testing and flow validation | Working prototype with end-to-end data flow<br>Initial test cases completed |
| **April 14–16**   | Enhancement & Documentation     | - Refine prompts (multi-shot, contextual)<br>- Polish UI/UX if applicable<br>- Document code and logic<br>- Start compiling technical notebook | Improved prompt quality<br>Well-documented codebase<br>Notebook draft |
| **April 18**      | Internal Review & Evaluation    | - Team demo of current build<br>- Review deliverables against goals<br>- Identify bugs, gaps, or improvements<br>- Align on submission strategy | Reviewed and validated prototype<br>List of final tasks and bug fixes |
| **April 19–20**   | Finalization & Submission       | - Final debugging and QA<br>- Finalize notebook with explanations and markdown<br>- Draft blogpost content<br>- Record and edit walkthrough video | Complete competition package:<br>• Notebook<br>• Blogpost<br>• Video<br>• Submission-ready repository |

---

## ✅ Task Checklist by Phase

### 📍 April 7 – Research & Exploration
- [x] Identify Gen AI applications in HR  
- [x] Research multi-agent systems  
- [x] Collect tools, datasets, and technologies  
- [x] Document findings in shared workspace  

---

### 📍 April 8 – Ideation & Planning
- [x] Conduct planning meeting  
- [x] Define project scope and goals  
- [x] Outline key features and limitations  
- [x] Determine input/output for the assistant  
- [x] Finalize technical stack and architecture  
- [x] Assign roles and responsibilities  

---

### 📍 April 9–11 – Initial Build
- [x] Set up development environment

### 🔹 Resume Parser Agent
- [ ] Replace placeholder with actual resume parsing logic (skills, roles, projects)
- [ ] Generate brief summarization about applicant  based on parsed resume
- [ ] Return brief summarization list in clean structure (e.g., JSON)

### 🔹 Interviewer Agent
- [ ] Build question-answer loop (ask → record → follow-up if needed)
- [ ] Handle multiple questions dynamically
- [ ] Integrate voice input/output cleanly (handle retries if audio fails)
- [ ] Save transcript (question + answer) to pass to evaluator

### 🔹 Evaluator Agent
- [ ] Analyze each response (clarity, relevance, confidence)
- [ ] Score each question or provide a final score
- [ ] Summarize strengths, weaknesses, and give **actionable feedback**
- [ ] Return evaluation report in structured format

### 🔹 Graph Improvements
- [ ] Add memory (optional) or feedback loop for interviewer (if time allows)
- [ ] Refactor state passing (resume → questions → responses → evaluation)
- [ ] Add logging/debug support to test each node individually

### 🔹 Optional Enhancements
- [ ] Add Gemini model support (instead of OpenAI)
- [ ] Design Streamlit UI or basic web interface for interaction
- [ ] Save/export interview sessions as PDFs or JSON reports

---

### 📍 April 12–13 – Integration & Testing
- [ ] Integrate all agents into a single workflow
- [ ] Enable user input for role and company
- [ ] Perform end-to-end testing of system
- [ ] Log and fix integration issues

---

### 📍 April 14–16 – Enhancement & Documentation
- [ ] Optimize prompts (multi-shot, role-specific)
- [ ] Add/clean up UI (optional but helpful)
- [ ] Document codebase with clear comments
- [ ] Draft technical notebook with markdown explanations

---

### 📍 April 18 – Internal Review
- [ ] Conduct team demo
- [ ] Review scope vs. delivery
- [ ] Finalize outstanding tasks
- [ ] Identify any critical bugs or missing elements

---

### 📍 April 19–20 – Finalization & Submission
- [ ] Final testing and bug fixes
- [ ] Finalize and polish notebook
- [ ] Write and edit blogpost
- [ ] Record and narrate demo video
- [ ] Submit all materials to competition portal

---

## 🏆 Competition Evaluation Criteria

| Deliverable   | Weight / Multiplier          | Evaluation Focus                                                                 |
|---------------|------------------------------|----------------------------------------------------------------------------------|
| **Notebook**  | Max 10 points                | - Creativity & originality of use case<br>- Suitability of Gen AI<br>- Clarity of documentation and explanation<br>- End-to-end walkthrough of solution |
| **Blogpost**  | Bonus multiplier (up to 1.5x)| - Communicates the problem and solution clearly<br>- Highlights implementation with code snippets<br>- Discusses limitations and future scope |
| **Video**     | Bonus multiplier (up to 1.5x)| - Visuals with voiceover<br>- Balanced technical explanation and storytelling |

> **Judges**: Gen AI experts from Google (Engineering & Marketing)
