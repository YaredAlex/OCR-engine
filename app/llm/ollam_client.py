import requests
import json
from ollama import Client
from langchain_ollama.llms import OllamaLLM

OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL = "llama3.1:8b"
MODEL = "gpt-oss:20b-cloud"
client = Client(host='http://localhost:11434')

llm_chain = OllamaLLM(
    model=MODEL, 
    temperature=0.0,
    reasoning=True
)

# method 1 using http request 
def call_llm(prompt: str) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "think":False,
        },
        timeout=120
    )
    response.raise_for_status()
    return response.json()["response"]

# method 2 using ollama client
def ollama_client(message:str)->str:
    # TODO convert message to list
    response = client.chat(model=MODEL,messages=[
        {
            "role":"user",
            "content":f"{message}"
        }
    ])

    return response

# method 3 using langchain
def ollama_chain(messages:list[str])->list[str]:
    return llm_chain.batch(messages)
