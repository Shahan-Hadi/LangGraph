import streamlit as st
from Agent_1 import agent_invoke

st.set_page_config(page_title="Agent Chat", page_icon="🤖")

# Initialize session state for chat sessions
if "sessions" not in st.session_state:
    st.session_state["sessions"] = [[]]  # List of sessions, each is a list of messages
    st.session_state["current_session"] = 0  # Index of current session
    st.session_state["last_input"] = ""

# Sidebar: List of chat sessions with dynamic titles
st.sidebar.title("Chat History")

# Button
if st.sidebar.button("➕ New Chat", key="new_chat"):
    st.session_state["sessions"].append([])
    st.session_state["current_session"] = len(st.session_state["sessions"]) - 1
    st.session_state["last_input"] = ""

# Generate dynamic titles for each session
def get_chat_title(session):
    for msg in session:
        if msg["role"] == "user":
            # Use the first 6 words of the first user message as the title
            return " ".join(msg["content"].split()[:6]) + ("..." if len(msg["content"].split()) > 6 else "")
    return "New Chat"

for idx, session in enumerate(st.session_state["sessions"]):
    title = get_chat_title(session)
    # Highlight the currently selected chat
    if idx == st.session_state["current_session"]:
        st.sidebar.markdown(f"**{title}**")
    else:
        if st.sidebar.button(title, key=f"session_{idx}"):
            st.session_state["current_session"] = idx
            st.session_state["last_input"] = ""  # Reset input for new session

current_session = st.session_state["current_session"]
messages = st.session_state["sessions"][current_session]

st.title("How can be of help? 🤖")
st.markdown("""
Type your message below and press Enter to chat.
""")

user_input = st.text_input("Ask:", "", key="input")

if st.button("Send") or (user_input and st.session_state.get("last_input") != user_input):
    if user_input:
        messages.append({"role": "user", "content": user_input})
        ai_response = agent_invoke(user_input)
        messages.append({"role": "ai", "content": ai_response})
        st.session_state["last_input"] = user_input

# Display chat history for current session (most recent at the top)
for msg in reversed(messages):
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**AI:** {msg['content']}")