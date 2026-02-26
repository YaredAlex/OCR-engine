import requests
import json
from ollama import Client
from langchain_ollama.llms import OllamaLLM

OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL = "llama3.1:8b"
# MODEL = "gpt-oss:20b-cloud"
# MODEL = "gpt-oss:20b"
# MODEL = "gemma3:1b"
# MODEL = "gemma3:1b-it-qat"
# MODEL = "qwen3:0.6b"
# MODEL = "qwen3:4b"
# MODEL = "gemma3:4b-cloud"
# MODEL = "ministral-3:8b"
# MODEL = "ministral-3:14b-cloud"
# MODEL = "ministral-3:3b-cloud"
MODEL = "ministral-3:3b-instruct-2512-q4_K_M"
client = Client(host='http://localhost:11434')

llm_chain = OllamaLLM(
    model=MODEL, 
    temperature=0.0,
    reasoning=False,
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
