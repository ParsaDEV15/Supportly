from langchain_openai import ChatOpenAI
from langchain_classic.agents import create_openai_tools_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from app.tools.retriever_tool import faq_tool
from app.tools.orders_getter_tool import get_order_status_tool
from app.tools.recommend_product_tool import recommend_product_tool
from langchain_core.runnables.history import RunnableWithMessageHistory
from config.settings import LLM_MODEL


class ChatBot:
    def __init__(self):
        chat_bot = ChatOpenAI(model=LLM_MODEL)

        system_prompt = open('app/prompts/system_prompt.txt', 'r', encoding='utf-8').read()

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