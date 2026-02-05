import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL = "llama3.1:8b"
MODEL = "gpt-oss:20b-cloud"

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
