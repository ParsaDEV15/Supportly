import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MONGODB_URI = os.getenv("MONGODB_URI")

DB_NAME = "customer_bot"
FAQ_COLLECTION = "faqs"
ORDER_COLLECTION = "orders"

EMBEDDING_MODEL = "text-embedding-3-small"
LLM_MODEL = "gpt-5-nano-2025-08-07"