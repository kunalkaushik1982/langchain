import requests
import streamlit as st

def get_openai_response(input_text):
    base_url = "http://localhost:8000/essay/invoke"
    payload = {'input': {'topic': input_text}}
    print(f"URL: {base_url}")
    print(f"Payload: {payload}")
    # Make the POST request
    response = requests.post(base_url, json=payload)
    #response = requests.post("http://localhost:8000/essay/invoke", json={'input': {'topic': input_text}})
    
    try:
        response_data = response.json()
        print(response_data)  # Debugging: Print API response
        # Use .get() to avoid KeyErrors and handle missing keys
        return response_data.get('output', {}).get('content', 'Response format invalid')
    except Exception as e:
        return f"Error: {e}, Response Content: {response.text}"



def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke",json={'input': {'topic': input_text}})
    try:
        response_data = response.json()
        # Debugging print to see the API response
        print(response_data)
        # Adjust the key lookup to match the actual response
        #return response_data.get('poem', 'No output key in response')
        return response_data.get('output', {}).get('content', 'Response format invalid')
    except Exception as e:
        # Handle unexpected response structure
        return f"Error: {e}, Response Content: {response.text}"


    ## streamlit framework

st.title('Langchain Demo With LLAMA3 API')
input_text=st.text_input("Write an essay on")
#input_text1=st.text_input("Write a poem on")

if input_text:
    st.write(get_openai_response(input_text))

# if input_text1:
#     st.write(get_ollama_response(input_text1))