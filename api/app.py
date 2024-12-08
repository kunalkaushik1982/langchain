from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os
import uvicorn

# Load environment variables
load_dotenv()

# Set OpenAI API key
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

# Initialize FastAPI
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

# Define models and prompts
openai_model = ChatOpenAI()
# ollama_model = Ollama(model="llama3")

essay_prompt = ChatPromptTemplate.from_template("Write me an essay about {topic} with 10 words")
# poem_prompt = ChatPromptTemplate.from_template("Write me a poem about {topic} for a 5-year-old child with 10 words")


# Define API endpoints
@app.post("/essay")
async def generate_essay(topic: str):
    """Generate an essay using the OpenAI model."""
    response = openai_model(essay_prompt.format_prompt(topic=topic).to_messages())
    return {"essay": response.content}


# @app.post("/poem")
# async def generate_poem(topic: str):
#     """Generate a poem using the Ollama model."""
#     response = ollama_model(poem_prompt.format_prompt(topic=topic).to_messages())
#     return {"poem": response.content}


# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
