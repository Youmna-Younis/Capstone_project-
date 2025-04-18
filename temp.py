# # from langgraph.graph import StateGraph, START, END
# from langchain_google_genai import ChatGoogleGenerativeAI

# # # Try using different models. The Gemini 2.0 flash model is highly
# # # capable, great with tools, and has a generous free tier. If you
# # # try the older 1.5 models, note that the `pro` models are better at
# # # complex multi-tool cases like this, but the `flash` models are
# # # faster and have more free quota.
# # # Check out the features and quota differences here:
# # #  - https://ai.google.dev/gemini-api/docs/models/gemini
# # from utils.gemini_utils import model

# from dotenv import load_dotenv
# load_dotenv()
# llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


# def chatbot(state: Bas) -> OrderState:
#     """The chatbot itself. A simple wrapper around the model's own chat interface."""
#     message_history = [BARISTABOT_SYSINT] + state["messages"]
#     return {"messages": [llm.invoke(message_history)]}


# # Set up the initial graph based on our state definition.
# graph_builder = StateGraph(OrderState)

# # Add the chatbot function to the app graph as a node called "chatbot".
# graph_builder.add_node("chatbot", chatbot)

# # Define the chatbot node as the app entrypoint.
# graph_builder.add_edge(START, "chatbot")

# chat_graph = graph_builder.compile()

















# #####WORK####################

# # from google import genai
# # Configure Gemini API
# # GOOGLE_API_KEY="AIzaSyBvE82VYWYZknp0g31a8WB6WvFQV_YbimE"
# # API_KEY = GOOGLE_API_KEY









# # Initialize the Gemini model
# # from google import genai

# # from langchain_google_genai import ChatGoogleGenerativeAI
# # # model = genai.GenerativeModel('gemini-2.0-flash')
# # client = genai.Client(api_key=GOOGLE_API_KEY)

# # def generate_response(prompt):
# #     """
# #     Generates a response using Gemini.
# #     """
# #     response = client.models.generate_content(
# #     model="gemini-2.0-flash",
# #     contents=prompt)

# #     # response = model.generate_content(prompt)
# #     return response.text.strip()
# # print(generate_response("hi"))







from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.state_schema import *
from nodes.resume_parser import parse_resume
from nodes.Interview_Preparation import prepare_interview_context
from utils.state_schema import *
# from nodes.interviewer import conduct_interview
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
# SYSTEM_INSTRUCTION = (
#         "You are HRInterviewBot, an intelligent and professional AI assistant designed to simulate real HR interviews. "
#         "A human (the candidate) will interact with you as part of a mock interview experience. "
#         "You will ask interview questions based on their resume and analyze their answers. "
#         "You are friendly, structured, and maintain a professional tone throughout the conversation.\n\n"
#         "Your responsibilities include:\n"
#         "- Asking tailored questions provided to you from the resume_parser agent\n"
#         "- Listening to the candidate’s responses (captured via voice or text)\n"
#         "- Logging each question and its corresponding answer in a structured format\n"
#         "- Optionally asking follow-up questions for clarity or depth\n"
#         "- Passing the transcript to the evaluator agent after the interview concludes\n\n"
#         "Interview rules:\n"
#         "- Do not deviate from interview-related topics\n"
#         "- Do not offer advice or feedback during the interview\n"
#         "- Always maintain a respectful and encouraging tone\n"
#         "- Ask one question at a time and wait for a full answer\n"
#         "- Confirm understanding if the answer is unclear or incomplete\n\n"
#         "When the candidate is finished answering all questions, thank them for their time and end the session gracefully.\n"
#         "If tools such as audio input or external resume parsing are not available yet, inform the user that those features are under development."
#     )
INIT_Prompt=""
WELCOME_MSG = (
    "Hi there! 👋 I'm your virtual interviewer.\n"
    "I'll ask you a few questions based on your resume—just answer like you would in a real interview.\n"
    "Ready? Let's get started!"
)
def chatbot(state: InterviewPreparationState) -> InterviewState:
    """The chatbot itself. A simple wrapper around the model's own chat interface."""

    message_history = [INIT_Prompt] + state["messages"]
    return {"messages": [llm.invoke(message_history)]}






def prepare_candidate_profile(resume: str, job_description: str):
    # Initial state
    initial_state: BaseState = {
        "resume": resume,
        "job_description": job_description,
        "stage": "start"
    }

    # Step 1: Parse the resume
    state = parse_resume(initial_state)
    if state["stage"] == "error":
        print("Error during resume parsing:", state.get("error"))
        return

    # Step 2: Prepare interview context
    state = prepare_interview_context(state)
    if state["stage"] == "error":
        print("Error during interview preparation:", state.get("error"))
        return 
    return state


    # # Step 4: Evaluate responses
    # state = evaluate_responses(state)
    # if state["stage"] == "error":
    #     print("Error during evaluation:", state.get("error"))
    #     return

    # # Final Output
    # print("\nInterview Complete!")
    # print("Evaluation:")
    # print(state["evaluation"])


def chatBot(state: InterviewPreparationState) -> InterviewState:
    """The chatbot itself. A simple wrapper around the model's own chat interface."""
    # Extract messages as a list of strings
    message_texts = [msg["message"] for msg in state["messages"]]
    
    # Combine llm_context with the extracted messages
    message_history = state["llm_context"] + " ".join(message_texts)
    
    # Invoke the LLM with the combined message history
    return {"messages": [llm.invoke(message_history)]}
resume = "/workspaces/Capstone_project-/data/resumeSample.pdf"
job_description = "Senior Software Engineer with expertise in Python and AI."


state=prepare_candidate_profile(resume,job_description)
print(f"stat e : {state}")
INIT_Prompt=state["llm_context"]
print(f"INIT_Prompt : {INIT_Prompt}")
# Set up the initial graph based on our state definition.
graph_builder = StateGraph(InterviewPreparationState)

# Add the chatbot function to the app graph as a node called "chatbot".
graph_builder.add_node("chatbot", chatbot)

# Define the chatbot node as the app entrypoint.
graph_builder.add_edge(START, "chatbot")

chat_graph = graph_builder.compile()
from pprint import pprint

user_msg = "Hello, what can you do?"
state = chat_graph.invoke({"messages": [user_msg]})

# The state object contains lots of information. Uncomment the pprint lines to see it all.
# pprint(state)

# Note that the final state now has 2 messages. Our HumanMessage, and an additional AIMessage.
for msg in state["messages"]:
    print(f"{type(msg).__name__}: {msg.content}")