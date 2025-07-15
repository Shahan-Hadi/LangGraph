############## DRAFTER ##########

from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage, AIMessage, BaseMessage
from langgraph.graph import add_messages
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langgraph.graph.message import add_messages

document_content = ""

class AgentState(TypedDict):
    messages : Annotated[Sequence[BaseMessage], add_messages]

@tool
def update(content: str) -> str:
    '''Update the document with the provided content'''
    global document_content
    document_content = content
    return f"Document has been updated successfully. Data is in: \n{document_content}"

@tool
def save(filename: str) -> str:
    '''Save the current file and finish the process

    Args:
        filename: Name for the text file'''
    
    global document_content

    if not filename.endswith('.txt'):
        filename = f"{filename}.txt"

    try:
        with open(filename, 'w') as file:
            file.write(document_content)
        print(f"\n Document has been saved to: {filename}")
        return f"Document has been saved successfully to '{filename}'"

    except Exception as e:
        return f"Error saving file: {str(e)}"
    
tools = [update, save]

llm = ChatOllama(model='llama3')

def process(state: AgentState) -> AgentState:
    prompt = SystemMessage(content= f"""
    You are Drafter, a helpful writing assistant. You are going to help the user update and modify documents.
    If the user wants to update or modify content, use the 'update' tool with the complete updated content.
    If the user wants to save and finish, you need to use the 'save' tool.
    Make sure to always show the current document state after modifications. 
    
    The current document content is:{document_content}""")

    if not state['messages']:
        msg = 'I am ready to help you update and save your documents'
        user_msg = HumanMessage(content=msg)
    else:
        user_input = input('\nHow can i help with your document ? ')
        print(f"\n User: {user_input}")
        user_msg = HumanMessage(content= user_input)
    
    all_messages = [prompt] + list(state['messages']) + [user_msg]

    response = llm.invoke(all_messages)

    print(f"\n AI: {response.content}")
    if hasattr(response, 'tool_calls') and response.tool_calls:
        print(f" USING TOOLS: {[tc['name'] for tc in response.tool_calls]}")

    return {"messages": list(state['messages']) + [user_msg, response]}

def decisive_node(state: AgentState) -> AgentState:
    '''Determine if we should continue or end the conversation'''
    
    messages = state['messages']

    if not messages:
        return 'continue'
    # This is used for most recent tool message...
    for message in reversed(messages):
        #...Adding check if there is ToolMEssage resulting from save
        if (isinstance(message, ToolMessage) and
            "saved" in message.content.lower() and
            "document" in message.content.lower()):
            return "end" #This will go the end of program
        
    return 'continue'

def print_message(messages):
    '''Function to display message i more readable format'''
    if not messages:
        return
    for message in messages[-3:] if len(messages) >=3 else messages:
        if isinstance(message, ToolMessage):
            print(f"\n Tool Result: {message.content}")

graph = StateGraph(AgentState)

graph.add_node('agent', process)
graph.add_node('tools', ToolNode(tools))

graph.set_entry_point('agent')

graph.add_edge('agent', 'tools')

graph.add_conditional_edges(
    'tools',
    decisive_node,
    {
        'continue': 'agent',
        'end': END,
    },
)

app = graph.compile()

def run_document_agent():
    print(f"\n *****Drafter*****")

    state = {'messages': []}

    for step in app.stream(state, stream_mode = 'values'):
        if 'messages' in step:
            print_message(step['messages'])

    print(f"\n *****Drafter*****")

if __name__ == "__main__":
    run_document_agent()