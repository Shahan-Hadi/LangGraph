# *******************Memory Retention****************

from typing import TypedDict, List, Union
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage, AIMessage
from langchain_ollama import ChatOllama

class AgentState(TypedDict):
     message: list[Union[HumanMessage, AIMessage]]

llm = ChatOllama(model='phi')

def process(state: AgentState) -> AgentState:
     response = llm.invoke(state['message'])

     state['message'].append(AIMessage(content=response.content))

     print(f"\nAI: {response.content}")


graph = StateGraph(AgentState)
graph.add_node('process', process)
graph.add_edge(START, 'process')
graph.add_edge('process', END)
agent = graph.compile()

conversation_history = []

user_input = input('Enter: ')

while user_input != 'exit':
    conversation_history.append(HumanMessage(content=user_input))
    result = agent.invoke({'message': conversation_history})
    conversation_history = result['message']
    user_input = input('Enter: ')

with open('Memory_retention.txt', 'w') as file:
     file.write('Your conversation log:\n')

     for message in conversation_history:
         if isinstance(message, HumanMessage):
               file.write(f"You: {message.content}")
         elif isinstance(message, AIMessage):
              file.write(f"AI: {message.content}")   

     file.write('End of conversation')

print('Conversation saved to Memory_retention.txt')