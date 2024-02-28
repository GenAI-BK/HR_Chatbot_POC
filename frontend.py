"""
This is a RAG model which uses beyondkey HR policyes.
Created By: 
Create Date: 
Last Updated Date:

Updates:
update on 23 Feb 2024 by Jugal:
    * Code mearge in stremlit app.
    * some fixes and updates
"""

import rag
import streamlit as st
import creds

#----------------- Setting -------------------------
api_key_openai = creds.api_key_openai
api_key_pinecone = creds.api_key_pinecone
directory = creds.directory
index_name=creds.index_name
#----------------- Setting -------------------------

def generate_response(input_data_query):
    chain= rag.ask_model(api_key_openai,api_key_pinecone,directory)
    question=input_data_query
    output = rag.perform_conversational_retrieval(chain, question)
    return output # Return the response

st.title("HR Policy Chatbot")

messages = st.empty()

if "messages" not in st.session_state:
    st.session_state["messages"] = []

def display_messages():
    for message in st.session_state["messages"]:
        if message["role"] == "user":
            st.chat_message("user").write(message["content"])
        else:
            st.chat_message("assistant").write(message["content"])


if prompt := st.chat_input():
    st.session_state["messages"].append({"role": "user", "content": prompt})
    response = generate_response(prompt)
    msg = response
    st.session_state["messages"].append({"role": "assistant", "content": msg['answer']})  # Access the content attribute of the message object
    st.session_state["messages"] = st.session_state["messages"][-100:]  # Limit the number of messages to 100
    display_messages()


