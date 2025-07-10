# 🤖 LangGraph Conversational Agents

Welcome to **LangGraph Conversational Agents**!  
This repository showcases two powerful AI-driven chatbot projects built with [LangGraph](https://www.langchain.dev/langgraph/) and [ChatOllama](https://ollama.com), along with a sleek **Streamlit UI** for an interactive web experience.

---

## 🌟 What’s Inside

1. 🗣️ **Agent 1** – A stateless chatbot powered by `llama3` for fast, one-shot conversations.
2. 🧠 **Agent 2** – A memory-enabled chatbot powered by `phi`, ideal for multi-turn, context-aware dialogues.
3. 💻 **Streamlit Web UI** – A modern interface to chat with Agent 1.

---

## 🚀 Project Overview

### 🗣️ Agent 1 — Simple Stateless Chatbot

> `File: Agent_1.py`

A fast, lightweight terminal chatbot that responds to each input independently, with no memory of past interactions.

#### ✨ Features

- ⚡ **Stateless**: No memory; each response is based solely on the current input.
- 🧠 **Powered by `llama3`** via ChatOllama.
- 🧩 **Built with LangGraph** for clear state flow.
- 🔧 Easily customizable for different prompt styles or specific tasks.

#### ▶️ How to Run

```bash
# Pull llama3 model
ollama pull llama3

# Install dependencies
pip install langgraph langchain_ollama langchain_core

# Run the chatbot
python Agent_1.py
