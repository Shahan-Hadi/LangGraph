# 🤖 LangGraph-Based Conversational Agents

This repository features two AI-powered agents built with [LangGraph](https://www.langchain.dev/langgraph/) and [ChatOllama](https://ollama.com):

1. 🗣️ **Agent 1 – A Simple BOT** (stateless, powered by `llama3`)
2. 🧠 **Agent 2 – Memory Retention BOT** (conversation history, powered by `phi`)
3. 💻 A Streamlit web UI for interacting with Agent 1

---

## 🧠 Projects Overview

### 1. 🗣️ Agent 1 — A Simple BOT (Stateless)

> `File: Agent_1.py`

A lightweight, terminal-based chatbot that uses the `llama3` model and handles one input at a time. Perfect for short, single-turn conversations.

#### 🔹 Features:
- Stateless (no memory of previous input)
- Built with LangGraph and ChatOllama
- Fast and minimal

#### ▶️ Run:
```bash
python Agent_1.py


# 🧠 Agent 2 — Memory Retention BOT

This project is a memory-enabled conversational AI built using [LangGraph](https://www.langchain.dev/langgraph/) and [ChatOllama](https://ollama.com). Unlike stateless chatbots, this agent remembers the full conversation and responds based on prior context, simulating more natural multi-turn dialogue.

---

## 🔍 Overview

- 📌 Maintains full conversation history
- 💬 Responds contextually using previous interactions
- 💾 Automatically logs the entire conversation to a `.txt` file
- 🧠 Powered by the `phi` language model via Ollama

---

## 🛠️ Technologies Used

- Python 3.8+
- [LangGraph](https://www.langchain.dev/langgraph/)
- [LangChain Core](https://python.langchain.com/docs/core/)
- [ChatOllama](https://python.langchain.com/docs/integrations/llms/ollama)
- `phi` language model from [Ollama](https://ollama.com)

---

## ▶️ How to Run

### 1. ✅ Prerequisites

- Make sure you have [Ollama installed](https://ollama.com/download).
- Pull the `phi` model:
  ```bash
  ollama pull phi

