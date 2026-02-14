import streamlit as st
import openai
import os

# ---------------------------
# Load OpenAI API Key
# ---------------------------
# On Streamlit Cloud, add your key under Settings → Secrets
openai.api_key = os.getenv("OPENAI_API_KEY")

# ---------------------------
# Function to get AI response
# ---------------------------
def ask_llm(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# ---------------------------
# Streamlit App UI
# ---------------------------
st.title("🤖 AI Chatbot (OpenAI + Streamlit)")

# Chat history memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input box
user_input = st.text_input("Type your question here:")

# Send button
if st.button("Send"):
    if user_input.strip() != "":
        with st.spinner("Thinking..."):
            reply = ask_llm(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("AI", reply))

# Reset button
if st.button("Reset Chat"):
    st.session_state.chat_history = []

# Display conversation
st.subheader("Conversation History")
for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**🧑 {speaker}:** {message}")
    else:
        st.markdown(f"**🤖 {speaker}:** {message}")
