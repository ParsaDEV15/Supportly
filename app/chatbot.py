from langchain_openai import ChatOpenAI
from langchain_classic.agents import create_openai_tools_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from tools.retriever_tool import faq_tool
from tools.orders_getter_tool import get_order_status_tool
from tools.recommend_product_tool import recommend_product_tool
from config.settings import LLM_MODEL


class ChatBot:
    def __init__(self):
        chat_bot = ChatOpenAI(model=LLM_MODEL)

        system_prompt = open('prompts/system_prompt.txt', 'r').read()

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}"),
            ('placeholder', '{agent_scratchpad}')
        ])

        tools = [faq_tool, get_order_status_tool, recommend_product_tool]

        agent = create_openai_tools_agent(
            llm=chat_bot,
            prompt=prompt,
            tools=tools
        )

        self.executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    def get_response(self, query):
        return self.executor.invoke({'input': query})


if __name__ == '__main__':
    chatbot = ChatBot()

    while True:
        prompt = input('Write your prompt: ')
        response: dict = chatbot.get_response(query=prompt)
        print(response['output'])