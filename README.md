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
- **MongoDB** - Stores orders and products data
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
├── README.md
└── streamlit_app.py
```
---

## 🚀 How to Use

Follow the steps below to run **Supportly** locally.

1. **Clone the repository**
```bash
git clone https://github.com/ParsaDEV15/Supportly.git
cd supportly
```

2. **Create and activate a virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

Create a `.env` file:
```env
OPENAI_API_KEY=your_openai_api_key
MONGODB_URI=your_mongodb_connection_string
```

5. **Set up the database**

Initialize MongoDB and populate it with sample data required by the chatbot.

```bash
python db/add_products.py
python db/create_orders.py
```

- **`db/add_products.py`**  
  Loads a predefined list of products from `products.json` and inserts them into the MongoDB products collection.  
  These products are used by the assistant to answer product-related questions and provide recommendations.

- **`db/create_orders.py`**  
  Creates and manages sample customer orders via a simple CLI interface. The script allows interactive order creation,  
  stores orders in the MongoDB orders collection, and supports viewing existing orders for testing order-status queries.


6. **Prepare the FAQ data**

First, generate and preprocess the FAQ data using the data pipeline script:

```bash
python data/data_pipeline.py
```

This step converts the raw FAQ content into a structured format suitable for embedding and retrieval.


7. **Build the vector store**

After the FAQ data is prepared, embed the documents into the vector database:

```bash
python app/embedding.py
```


This step generates vector embeddings and stores them for use in the RAG-based retrieval system.

8. **Run the application**
```bash
streamlit run streamlit_app.py
```

You can now interact with the assistant to ask FAQ-related questions, check order status, and receive product recommendations.

**Notes:**
- Ensure MongoDB is running before starting the application
- FAQ embeddings only need to be generated once unless the data changes