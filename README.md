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
