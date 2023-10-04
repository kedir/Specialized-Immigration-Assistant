import streamlit as st
import requests
import json
import time

st.title("Immigration Guidance System")

url = 'http://backendservice:8000/text/predict'

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
# prompt = ""
if prompt :=  st.chat_input("Send a message"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

if prompt != None:
    data = {"question": str(prompt)}
    print(data)
    assistant_response = requests.post(url, json = data)
    assistant_response = assistant_response.json()
    print(assistant_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": assistant_response['text_tokens']['response']})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        for chunk in assistant_response['text_tokens']['response'].split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
    message_placeholder.markdown(full_response)
# Add assistant response to chat history
# st.session_state.messages.append({"role": "assistant", "content": full_response})