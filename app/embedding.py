from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_chroma.vectorstores import Chroma
from config.settings import OPENAI_API_KEY, VECTORS_SAVE_PATH
import os

loader = CSVLoader(file_path='../data/cleaned_data/FAQs.csv')
documents = loader.load()

embedding = OpenAIEmbeddings(
    model='text-embedding-3-small',
    request_timeout=20,
    max_retries=5
)

os.makedirs(VECTORS_SAVE_PATH, exist_ok=True)

Chroma.from_documents(
    embedding=embedding,
    documents=documents,
    persist_directory=VECTORS_SAVE_PATH,
    collection_name="FAQs"
)