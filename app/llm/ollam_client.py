import requests
import json
from ollama import Client

OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL = "llama3.1:8b"
MODEL = "gpt-oss:20b-cloud"
client = Client(host='http://localhost:11434')

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

def ollama_client(messages:list[str])->str:
    response = client.chat(model=MODEL,messages=[
        {
            "role":"user",
            "content":""
        }
    ])

    return response
