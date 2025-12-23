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

---

## 🧱 Tech Stack

- **LangChain** – LLM orchestration and agent framework
- **OpenAI GPT-5-nano-2025-08-07** – Language model backend
- **Chroma** – Stores FAQ documents
- **MongoDB** - Stores orders and supplies data
- **Streamlit** – Frontend
- **Python 3.12+**

---

## 📁 Project Structure

```bash
supportly/
├── app
│   ├── prompts/
│   ├── tools/
│   ├── chatbot.py
│   ├── embedding.py
│   └── retriever.py
│
├── config
├── └── settings.py
├── data
├── └── data_pipeline.py
├── db
│   ├── add_products.py
│   ├── create_orders.py
│   ├── mongo_setup.py
│   └── products.json
├── requirements.txt
└── README.md