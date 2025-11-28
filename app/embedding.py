from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_chroma.vectorstores import Chroma
from config.settings import BASE_DIR, VECTORS_SAVE_PATH
import os

csv_file_path = os.path.join(BASE_DIR, 'data', 'cleaned_data', 'FAQs.csv')
loader = CSVLoader(file_path=csv_file_path)
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

print(f'FAQs.csv file has been embedded and saved to: {VECTORS_SAVE_PATH}')