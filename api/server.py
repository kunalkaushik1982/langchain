from fastapi import FastAPI,Request
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
#from langchain_community.llms import ollama
import ollama
from dotenv import load_dotenv
import os
import uvicorn

# Load environment variables
load_dotenv()

# Set OpenAI API key
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

# Initialize FastAPI app
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="LangChain-powered API for essay and poem generation"
)

# Define models
openai_model = ChatOpenAI()
ollama_model = ollama.chat(model="llama3")


# Define prompts
essay_prompt = ChatPromptTemplate.from_template("Write an essay about {topic} with 10 words.")
poem_prompt = ChatPromptTemplate.from_template("Write a short and funny poem about {topic} in 20 words")

# Endpoints
@app.post("/essay")
async def generate_essay(request: Request):  
    """Generate an essay using the OpenAI model."""
    # Log the request body and headers
    body = await request.json()
    # headers = dict(request.headers)
    # print(f"Received Request: {body}")
    # print(f"Headers: {headers}")
    topic=body.get("topic")
    messages = essay_prompt.format_prompt(topic=topic).to_messages()
    response = openai_model(messages)
    
    return {"essay": response.content}

@app.post("/poem")
async def generate_poem(request: Request):
    """Generate a poem using the Ollama model."""
    # Log the request body and headers
    body = await request.json()
    # headers = dict(request.headers)
    # print(f"Received Request: {body}")
    # print(f"Headers: {headers}")
    topic = body.get("topic")
    messages=[{"role": "user", "content": f"Write a poem about {topic} for a 5-year-old child."}]
    response = ollama.chat(model="mistral", messages=messages)
    #poem=response.message.content
    poem=response.message.get("content","No text returned from Ollama model")
    return {"poem": poem}

# Run server
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
