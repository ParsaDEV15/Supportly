from langchain_openai import ChatOpenAI
from langchain_classic.agents import create_openai_tools_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_classic.memory import ConversationBufferWindowMemory
from app.tools.retriever_tool import faq_tool
from app.tools.orders_getter_tool import get_order_status_tool
from app.tools.recommend_product_tool import recommend_product_tool
from config.settings import LLM_MODEL


class ChatBot:
    def __init__(self):
        chat_bot = ChatOpenAI(model=LLM_MODEL)

        prompt_text = open('app/prompts/system_prompt.txt', 'r', encoding='utf-8').read()

        prompt = ChatPromptTemplate.from_messages([
            ("system", prompt_text),
            ('placeholder', '{chat_history}'),
            ("human", "{input}"),
            ('placeholder', '{agent_scratchpad}')
        ])

        tools = [faq_tool, get_order_status_tool, recommend_product_tool]

        chat_history = StreamlitChatMessageHistory(key="supportly_user")

        memory = ConversationBufferWindowMemory(
            llm=chat_bot,
            chat_memory=chat_history,
            return_messages=True,
            memory_key="chat_history",
            k=5
        )

        agent = create_openai_tools_agent(
            llm=chat_bot,
            prompt=prompt,
            tools=tools,
        )

        self.executor_with_memory = AgentExecutor(
            agent=agent,
            tools=tools,
            memory=memory,
            verbose=True,
        )

    def get_response(self, query):
        return self.executor_with_memory.invoke(
            {'input': query}
        )
