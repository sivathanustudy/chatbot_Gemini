import streamlit as st
import google.generativeai as genai
import os

st.title("Sample Bot 🤖🧠🇦🇮👾")
genai.configure(api_key = type access key)

if "messages" not in st.session_state:
    st.session_state.messages = []

for  message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Type your message here...")


if prompt:
    
    with st.chat_message("user"):
        st.markdown(prompt)

    msg = {"role": "user", "content": prompt}
    st.session_state.messages.append(msg)

    model = genai.GenerativeModel(model_name = "gemini-1.5-flash")
    response = model.generate_content(prompt).text

    with st.chat_message("assistant"):
        st.markdown(response)
