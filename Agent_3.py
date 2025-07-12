#******ReAct Agent (Reasoning and Acting Agent)******
from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langchain_core.messages import ToolMessage
from langchain_core.messages import HumanMessage

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

@tool
def add(a: int, b: int):
    '''This is an addition tool'''
    return a+b

@tool
def subtract(a: int, b:int):
    '''Subtraction Function'''
    return a-b

@tool
def multiply(a: int, b:int):
    '''multiplication Function'''
    return a*b


tools = [add, subtract, multiply]
llm = ChatOllama(model='llama3')

def process(state: AgentState) -> AgentState:
    prompt = SystemMessage(content= 'You are my AI assitant, please answer my query to the best of your knowledge')
    response = llm.invoke([prompt] + state['messages'])
    return {'messages': [response]}

def decisive_node(state: AgentState):
    messages = state['messages']
    last_message = messages[-1]
    if not last_message.tool_calls:
        return 'end'
    else:
        return 'continue'
    
graph = StateGraph(AgentState)
graph.add_node('agent', process)

tool_nod = ToolNode(tools=tools)
graph.add_node('tools', tool_nod)

graph.set_entry_point('agent')

graph.add_conditional_edges(
    'agent',
    decisive_node,{
        'continue': 'tools',
        'end': END,
    }, 
)
graph.add_edge('tools', 'agent')

app = graph.compile()

def print_stream(stream):
    for s in stream:
        message = s['messages'][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()

inputs = {'messages': [( 'Add 9 + 2 and then multiply it by 7')]}
print_stream(app.stream(inputs, stream_mode='values'))