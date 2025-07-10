🤖 LangGraph-Based Conversational Agents
This repository features two AI-powered conversational agents built with LangGraph and ChatOllama, along with a Streamlit web UI for interacting with Agent 1:

🗣️ Agent 1 – Simple BOT (stateless, powered by llama3)
🧠 Agent 2 – Memory Retention BOT (conversation history, powered by phi)
💻 Streamlit Web UI (for interacting with Agent 1)


🧠 Projects Overview
1. 🗣️ Agent 1 — Simple BOT (Stateless)

File: Agent_1.py

A lightweight, terminal-based chatbot powered by the llama3 model. It processes one input at a time, making it ideal for short, single-turn conversations without retaining context.
🔹 Features:

Stateless (no memory of previous interactions)
Built with LangGraph and ChatOllama
Fast and minimal for quick responses

▶️ How to Run:

Install Ollama and pull the llama3 model:ollama pull llama3


Install required Python packages:pip install langgraph langchain langchain-ollama


Run the script:python Agent_1.py


Interact with the bot in the terminal.

💻 Streamlit Web UI:
A web interface is provided to interact with Agent 1.

Install Streamlit:pip install streamlit


Run the Streamlit app (assuming app.py):streamlit run app.py


Access the UI at http://localhost:8501.


2. 🧠 Agent 2 — Memory Retention BOT

File: Agent_2.py

A conversational AI that retains the full conversation history, enabling contextual, multi-turn dialogue. Powered by the phi model, it logs all interactions to a .txt file for record-keeping.
🔹 Features:

Maintains full conversation history
Responds contextually based on prior interactions
Automatically logs conversations to a .txt file
Built with LangGraph and ChatOllama
Powered by the phi language model

▶️ How to Run:

Install Ollama and pull the phi model:ollama pull phi


Install required Python packages:pip install langgraph langchain langchain-core langchain-ollama


Run the script:python Agent_2.py


Engage in multi-turn conversations in the terminal. Conversations are saved to a .txt file.


🛠️ Technologies Used

Python: 3.8 or higher
LangGraph: For building conversational workflows
LangChain Core: Core components for Agent 2
ChatOllama: Integration with Ollama models (llama3 and phi)
Streamlit: Web interface for Agent 1
Ollama: Local model hosting for llama3 and phi


✅ Prerequisites

Install Ollama and ensure it’s running (ollama serve).
Pull the required models:ollama pull llama3
ollama pull phi


Install Python dependencies:pip install langgraph langchain langchain-core langchain-ollama streamlit




📝 Notes

Ensure Ollama is running locally before executing scripts.
Verify model availability (llama3 for Agent 1, phi for Agent 2).
The Streamlit UI is currently designed for Agent 1 only.
Check for dependency version compatibility if errors occur.
