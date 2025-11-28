from app.retriever import Retriever
from langchain_core.tools import Tool

retriever = Retriever()


def faq_retriever_func(query):
    results = retriever.get_retriever(query)
    return results


faq_tool = Tool(
    name='faqs_search',
    description='Use this tool to answer the general FAQs using documents.',
    func=faq_retriever_func
)