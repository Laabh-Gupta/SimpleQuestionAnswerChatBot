import os
import pathlib
import textwrap
import streamlit as st
import google.generativeai as genai
from langchain.schema import AIMessage, HumanMessage, SystemMessage

api_key1 = os.environ.get("GOOGLE_API_KEY")
if not api_key1:
    print("GOOGLE_API_KEY environment variable is not set.")
else:
    genai.configure(api_key=api_key1)

st.title("Simple Question and answer chat bot application")
st.header("Type your message:")

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

def output(question):
    response = chat.send_message(question)
    return response.text

def get_text():
    input_text = st.text_input("You: ")
    return input_text

user_input = get_text()
submit = st.button('Generate')

if submit:
    response = output(user_input)
    st.subheader("Answer:")
    st.write(response)