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

        vector_store = Chroma(
            embedding_function=embedding,
            persist_directory=VECTORS_SAVE_PATH,
            collection_name="FAQs"
        )

        self.retriever = vector_store.as_retriever(
            search_type='mmr',
            search_kwargs={'fetch_k': 7, 'k': 4}
        )

    def get_retriever(self, query):
        docs = self.retriever.invoke(input=query)
        return docs