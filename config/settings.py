import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MONGODB_URI = os.getenv("MONGODB_URI")

DB_NAME = "customer_bot"
FAQ_COLLECTION = "faqs"
ORDER_COLLECTION = "orders"

EMBEDDING_MODEL = "text-embedding-3-small"
LLM_MODEL = "o3-mini-2025-01-31"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VECTORS_SAVE_PATH = os.path.join(BASE_DIR, "data", "chroma_store")