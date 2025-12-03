from app.retriever import Retriever
from langchain_core.tools import Tool


def faq_retriever(query: str) -> str:
    retriever = Retriever()
    docs = retriever.get_retriever(query)

    if not docs:
        return "No relevant information found in the FAQs."

    return "\n\n".join([doc.page_content for doc in docs])


faq_tool = Tool(
    name='faqs_search',
    description='Use this tool to answer the general FAQs using documents.',
    func=faq_retriever
)