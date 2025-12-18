from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_message_histories import ChatMessageHistory
from config.settings import LLM_MODEL

summarizer_llm = ChatOpenAI(model=LLM_MODEL)

history = ChatMessageHistory()

history.add_user_message("Hi, I need help with my order.")
history.add_ai_message("Sure! Could you provide your order ID?")
history.add_user_message("My order ID is #12345.")
history.add_ai_message("Thank you! Your order is currently being processed.")


def summarize_messages(chat_history, top_k_messages):
    history = chat_history.messages[top_k_messages:]

    prompt_text = open('app/prompts/memory_llm_prompt.txt', 'r', encoding='utf-8').read()

    prompt = ChatPromptTemplate([
        ('system', prompt_text),
        ('placeholder', '{chat_history}')
    ])

    summarizer_chain = prompt | summarizer_llm

    result = summarizer_chain.invoke({"chat_history": history})

    print('New summary message:', result.content)


if __name__ == '__main__':
    summarize_messages(history, top_k_messages=5)