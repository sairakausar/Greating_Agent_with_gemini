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

def greating(state:State):
    """Ask the answer like Aslam o Alikum to replay walicum Salam,
    Hello to hi"""

    """If some body say greating in any language you say replay in that
    language"""

    """You ask replay in very respective and decent way """
    print("greeting node")
builder : StateGraph = StateGraph(State)


builder.add_node("Greating", greating)

builder.add_edge(START, "Greating")
builder.add_edge("Greating", END)

graph : CompiledStateGraph = builder.compile()
RESULT =graph.invoke({"great":"Hello"})
print(RESULT)




