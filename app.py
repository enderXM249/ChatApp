import streamlit as st
import google.generativeai as genai
import os

#llm part

# Configure API key
os.environ['GOOGLE_API_KEY'] = 'AIzaSyBLGA1PievJi5E1vTIjPoB0N2lEeYS8HWU'
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# model = genai.GenerativeModel(model_name="gemini-pro")

# streamlit main app

st.title("ChatBot🤖")

# Model selection
model_option = st.selectbox(
    "Choose a model:",
    ("gemini-pro", "gemini-1.5-pro")
)
# Initialize the Generative AI model based on user selection
@st.cache_resource
def get_model(model_name):
    model = genai.GenerativeModel(model_name=model_name)
    return model

model = get_model(model_option)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
   
    st.session_state.messages.append({"role": "user", "content": prompt})

    # response = f"Echo: {prompt}"
    response = model.generate_content(prompt)
    # response = model_response(model_option,model,prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response.text)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response.text})
