import streamlit as st
import requests

st.title("💬 IdeaMate — Corporate Suggestion Chatbot")
st.write("Ask for ideas, feedback, or suggestions on corporate topics!")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat input
user_message = st.chat_input("Type your question or idea request...")

if user_message:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_message})

    # Send to Flask API
    with st.spinner("Thinking..."):
        response = requests.post("http://127.0.0.1:5000/chat", json={"message": user_message})
        if response.status_code == 200:
            bot_reply = response.json()["reply"]
        else:
            bot_reply = "⚠️ Sorry, something went wrong with the server."

    # Add bot reply to chat history
    st.session_state.messages.append({"role": "bot", "content": bot_reply})

# Display messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])
