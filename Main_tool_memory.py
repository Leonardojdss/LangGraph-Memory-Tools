import json
from typing import Annotated
from typing_extensions import TypedDict

from dotenv import load_dotenv

from langchain_community.tools import YouTubeSearchTool
from langchain_tavily import TavilySearch
from langchain.chat_models import init_chat_model
from langchain.schema import AIMessage

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

load_dotenv()

tool_search = TavilySearch(max_results=2)
youtube = YouTubeSearchTool(verbose=True)
tools = [tool_search, youtube]

llm = init_chat_model("openai:gpt-4.1")

class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

llm_with_tools = llm.bind_tools(tools)

def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

graph_builder.add_node("chatbot", chatbot)

tool_node = ToolNode(tools=[tool_search, youtube])
graph_builder.add_node("tools", tool_node)

graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition)
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")

memory = MemorySaver()
graph = graph_builder.compile(checkpointer=memory)

config = {
    "configurable": {
        "thread_id": "1"
    }
}

def stream_graph_updates(user_input: str):
    last_message = None
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]},
                              config,
                              stream_mode="values"):
        for value in event.values():
            for msg in value:
                if isinstance(msg, AIMessage):
                    last_message = msg
    if last_message:
        print("Assistant:", last_message.content[-1] if isinstance(last_message.content, list) else last_message.content)

while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        stream_graph_updates(user_input)
    except Exception as e:
        print(f"An error occurred: {e}")
        print("An error occurred. Please restart chat.")
        break