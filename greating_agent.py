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
    input_state = state["greating"]
    response= llm.invoke(""" you are the agent give me greating output of """)
    print(response)

builder : StateGraph = StateGraph(State)


builder.add_node("Greating", greating)

builder.add_edge(START, "Greating")
builder.add_edge("Greating", END)

graph : CompiledStateGraph = builder.compile()
RESULT =graph.invoke({"great":"Hello"})
print(RESULT)

# #    ...................
 
# from typing_extensions import TypedDict
# from langgraph.graph import StateGraph, START, END
# from langgraph.graph.state import CompiledStateGraph
# from langchain_google_genai import ChatGoogleGenerativeAI 
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Initialize the LLM
# llm: ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash", api_key=os.getenv("GOOGLE_API_KEY")
# )

# # Define the state structure
# class State(TypedDict):
#     great: str
#     response: str

# # Define the greeting function
# def greating(state: State) -> State:
#     """Generate a response to a greeting using the LLM."""
#     print("greeting node")
#     input_text = state["great"]
#     # Query the LLM for a response
#     response = llm.invoke(f"Reply to the greeting '{input_text}' in a respectful way.")
#     # Update the state with the response
#     state["response"] = response
#     return state

# # Build the state graph
# builder: StateGraph = StateGraph(State)

# builder.add_node("Greating", greating)

# builder.add_edge(START, "Greating")
# builder.add_edge("Greating", END)

# # Compile the graph
# graph: CompiledStateGraph = builder.compile()

# # Invoke the graph
# result = graph.invoke({"great": "Aslam o Alaikum"})
# print(result)

# ##########............


