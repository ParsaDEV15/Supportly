from langchain_openai import ChatOpenAI
from langchain_classic.agents import create_openai_tools_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from config.settings import LLM_MODEL


class ChatBot:
    def __init__(self):
        chat_bot = ChatOpenAI(model=LLM_MODEL, temperature=0.1)

        system_prompt = open('prompts/system_prompt.txt', 'r').readline()

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}")
        ])

        self.chain = prompt | chat_bot

    def get_response(self, query):
        return self.chain.invoke({'input': query}).content


if __name__ == '__main__':
    chatbot = ChatBot()
    response = chatbot.get_response(query='Hello')
    print(response)