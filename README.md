# 🧠 Supportly — AI Customer Assistant Chatbot

**Supportly** is a smart customer support assistant powered by Large Language Models (LLMs), built using **LangChain**, **RAG (Retrieval-Augmented Generation)**, and **MongoDB**. It provides accurate, real-time assistance to customers by answering FAQs, checking order status, and recommending products.

This project demonstrates how to build a production-ready AI assistant with a vector database, tool-augmented agents, and natural language interfaces.

---

## ✨ Features

- ✅ Natural language chatbot interface
- 🔍 RAG-based retrieval from embedded FAQ knowledge
- 📦 Order status lookup via MongoDB backend
- 💡 Product recommendation support (static or future ML-based)
- 🔧 Modular and extensible with LangChain tools
- ☁️ Ready for cloud deployment (OpenAI, MongoDB Atlas)

---

## 🧱 Tech Stack

- **LangChain** – LLM orchestration and agent framework
- **OpenAI GPT-4 / GPT-3.5** – Language model backend
- **MongoDB** – Stores order data and FAQ documents
- **MongoDB Vector Search or Chroma** – Vector embeddings for RAG
- **Streamlit or FastAPI** – Frontend / interface layer
- **Python 3.10+**

---

## 📁 Project Structure

```bash
supportly/
├── app/               # Core app logic (agent, retriever, tools)
│   ├── chatbot.py
│   ├── retriever.py
│   ├── tools/
│   └── prompts/
├── db/                # MongoDB setup and vector store
├── data/              # FAQ and order data (CSV/JSON)
├── config/            # API keys and environment config
├── requirements.txt
└── README.md
