import streamlit as st
from app.chatbot import ChatBot


class App:
    def __init__(self):
        st.set_page_config(page_title="Supportly Chatbot", page_icon="🤖")

        st.title("🤖 Supportly — Customer Service Assistant")
        st.write("Ask about FAQs, order status, or product recommendations.")

        st.session_state.chatbot = ChatBot()

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            role = msg["role"]
            content = msg["content"]

            if role == "user":
                st.chat_message("user").markdown(content)
            else:
                st.chat_message("assistant").markdown(content)

    def run(self):
        user_input = st.chat_input("How can I assist you today?")

        if user_input:
            st.chat_message("user").markdown(user_input)

            st.session_state.messages.append({"role": "user", "content": user_input})

            bot_reply: dict = st.session_state.chatbot.get_response(user_input)['output']

            st.chat_message("assistant").markdown(bot_reply)

            st.session_state.messages.append({"role": "assistant", "content": bot_reply})


if __name__ == '__main__':
    App().run()