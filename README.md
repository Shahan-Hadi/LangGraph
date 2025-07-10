🤖 [Your Repository Name] - LangGraph Conversational Agents
Welcome to [Your Repository Name]! This repository showcases two powerful AI conversational agents built with LangGraph and ChatOllama, plus a sleek Streamlit web UI for an interactive experience.
🌟 What’s Inside:

🗣️ Agent 1: A stateless chatbot powered by llama3 for quick, one-off conversations.
🧠 Agent 2: A memory-enabled chatbot powered by phi, perfect for contextual, multi-turn dialogues.
💻 Streamlit Web UI: A user-friendly interface to interact with Agent 1.


🚀 Project Overview
🗣️ Agent 1 — Simple Stateless Chatbot

File: Agent_1.py

A fast, lightweight chatbot that responds to single inputs without retaining conversation history. Ideal for quick queries and simple interactions.
✨ Features

Stateless: No memory of past interactions for snappy responses.
Powered by llama3: Leverages the llama3 model via ChatOllama.
Built with LangGraph: Ensures a robust conversational framework.
[Custom Feature]: Add your unique feature here (e.g., custom prompts, specific use cases).

🛠️ How to Run

Install Ollama and pull the llama3 model:ollama pull llama3


Install Python dependencies:pip install langgraph langchain langchain-ollama


Launch the chatbot:python Agent_1.py


Start chatting in the terminal!

🌐 Streamlit Web UI
Interact with Agent 1 through a polished web interface.

Install Streamlit:pip install streamlit


Run the Streamlit app (assumes app.py):streamlit run app.py


Open http://localhost:8501 in your browser.


🧠 Agent 2 — Memory Retention Chatbot

File: Agent_2.py

A smart conversational AI that remembers the full conversation history, enabling natural, context-aware multi-turn dialogues. Conversations are automatically saved to a .txt file for easy reference.
✨ Features

Conversation Memory: Retains context for seamless, multi-turn interactions.
Powered by phi: Uses the phi model for efficient and accurate responses.
Chat Logging: Saves all conversations to a .txt file.
Built with LangGraph: Leverages LangGraph and LangChain Core for robust dialogue management.
[Custom Feature]: Add your unique feature here (e.g., sentiment analysis, custom memory retention).

🛠️ How to Run

Install Ollama and pull the phi model:ollama pull phi


Install Python dependencies:pip install langgraph langchain langchain-core langchain-ollama


Launch the chatbot:python Agent_2.py


Engage in multi-turn conversations, with logs saved to a .txt file.


🛠️ Technologies Used

🐍 Python: Version 3.8 or higher
🌐 LangGraph: For building conversational workflows
🔗 LangChain Core: Core components for Agent 2
🤖 ChatOllama: Integration with llama3 and phi models
🎨 Streamlit: Web interface for Agent 1
⚙️ Ollama: Local hosting for llama3 and phi models


📋 Prerequisites
Before running the agents, ensure the following:

Install Ollama and start the server:ollama serve


Pull the required models:ollama pull llama3
ollama pull phi


Install Python dependencies:pip install langgraph langchain langchain-core langchain-ollama streamlit


📝 Notes

Ensure Ollama is running (ollama serve) before executing scripts.
Verify model availability (llama3 for Agent 1, phi for Agent 2).
The Streamlit UI currently supports Agent 1 only; extend it for Agent 2 if desired.
Check for dependency version compatibility if you encounter errors.
Conversation logs for Agent 2 are saved to a .txt file in the project directory (customize the file path as needed).
