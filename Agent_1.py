# **A Simple BOT**

from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage


class AgentState(TypedDict):
    messages : List[HumanMessage]

llm = ChatOllama(model='phi')

def process(state: AgentState) -> AgentState:
    response = llm.invoke(state['messages'])
    print(f"\nAI: {response.content}")
    
    return state

graph = StateGraph(AgentState)
graph.add_node('process', process)
graph.add_edge(START, 'process')
graph.add_edge('process', END)
agent = graph.compile()

user_input = input('Enter: ')

while user_input != 'exit':
    agent.invoke({'messages' : [HumanMessage(content=user_input)]})
    user_input = input('Enter: ')