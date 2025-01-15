from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.state import CompiledStateGraph
from langchain_google_genai import ChatGoogleGenerativeAI 
import os
from dotenv import load_dotenv

load_dotenv()

llm: ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", api_key=os.getenv("GOOGLE_API_KEY")
)

class State(TypedDict):
    great: str
    response: str

def greating(state:State):
    """Ask the answer like Aslam o Alikum to replay walicum Salam,
    Hello to hi"""

    """If some body say greating in any language you say replay in that
    language"""

    """You ask replay in very respective and decent way """
    print("greeting node")
    input_state = state["great"]
    # response= llm.invoke(f"you are the agent give me greating output of my Question{input_state}")
    response= llm.invoke(f"you are the greeting chat bot agent and dont explain meaning but atleast use 7 words and be smart and try to one best answer in any culture or religious way for this {input_state}")
    print("response",response)

builder : StateGraph = StateGraph(State)

builder.add_node("Greating", greating)

builder.add_edge(START, "Greating")
builder.add_edge("Greating", END)

graph : CompiledStateGraph = builder.compile()
RESULT =graph.invoke({"great":"Aslam o Alikum"})
print(RESULT)



