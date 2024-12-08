import requests
import streamlit as st

# Functions for interacting with the server
def get_openai_response(topic):
    """Send a topic to the essay endpoint and get the response."""
    url = "http://localhost:8000/essay"
    payload = {"topic": topic}
    print(f"URL: {url}")
    print(f"Payload: {payload}")
    try:
        response = requests.post(url, json=payload)
        response_data = response.json()
        return response_data.get("essay", "No essay from server.")
    except Exception as e:
        return f"Error: {e}"

def get_ollama_response(topic):
    """Send a topic to the poem endpoint and get the response."""
    url = "http://localhost:8000/poem"
    payload = {"topic": topic}
    print(f"URL: {url}")
    print(f"Payload: {payload}")
    try:
        response = requests.post(url, json=payload)
        response_data = response.json()
        return response_data.get("poem", "No poem from server.")
    except Exception as e:
        return f"Error: {e}"

# Streamlit Interface
st.title("LangChain Client with OpenAI and Llama3")

# Input fields
essay_topic = st.text_input("Enter a topic for the essay:")
poem_topic = st.text_input("Enter a topic for the poem:")

# Buttons and Responses
if st.button("Generate Essay"):
    if essay_topic:
        st.write("### Essay:")
        st.write(get_openai_response(essay_topic))
    else:
        st.warning("Please enter a topic for the essay.")

if st.button("Generate Poem"):
    if poem_topic:
        st.write("### Poem:")
        st.write(get_ollama_response(poem_topic))
    else:
        st.warning("Please enter a topic for the poem.")
