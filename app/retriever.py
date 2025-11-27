from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_chroma.vectorstores import Chroma
from config.settings import VECTORS_SAVE_PATH


class Retriever:
    def __init__(self):
        embedding = OpenAIEmbeddings(
            model='text-embedding-3-small',
            request_timeout=20,
            max_retries=5
        )

        self.vector_store = Chroma(
            embedding_function=embedding,
            persist_directory=VECTORS_SAVE_PATH,
            collection_name="FAQs"
        )

    def get_retriever(self, query, k=3):
        return self.vector_store.similarity_search(query, k=k)