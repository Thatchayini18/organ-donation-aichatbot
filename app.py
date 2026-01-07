import streamlit as st
from chatbot import chatbot_response

st.set_page_config(page_title="Organ Donation AI Chatbot")

st.title("🫀 Organ Donation AI Assistant")
st.caption("24×7 Support for Donors and Recipients")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask your question here...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    response = chatbot_response(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.rerun()

if st.button("🔄 Clear Chat"):
    st.session_state.messages = []
    st.rerun()
