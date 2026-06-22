import requests
import json
from ollama import Client
from langchain_ollama.llms import OllamaLLM
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from typing import Dict,List,Any
import time
from openai import OpenAI

load_dotenv(override=True)

MODEL_NAME: str = "deepseek-v4-flash"
_MAX_RETRIES: int = 2
API_KEY = os.getenv("API_KEY",None)
BASE_URL: str = "https://api.deepseek.com/v1/chat/completions"
OLLAMA_URL = "http://localhost:11434/api/generate"
LOCAL = os.getenv("LOCAL",False)
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

if not LOCAL:
    llm_chain = ChatOpenAI(
    model="deepseek-chat",
    openai_api_key=API_KEY, 
    openai_api_base="https://api.deepseek.com/v1", 
    temperature=0
)

# method 1 using http request 
def call_llm(prompt: str) -> str:
    if not LOCAL:
        return send_to_agent(prompt)
    
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


def post_with_retry(payload: Dict[str, Any]) -> Dict[str, Any]:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    delay = 1

    for attempt in range(1, _MAX_RETRIES + 1):
        resp = requests.post(BASE_URL, json=payload, headers=headers, timeout=120)

        if resp.status_code == 429 or resp.status_code >= 500:
            if attempt == _MAX_RETRIES:
                resp.raise_for_status()

            print(
                f"\n  [{resp.status_code}] Retrying in {delay:.0f}s ({attempt}/{_MAX_RETRIES})...",
                end="",
                flush=True,
            )
            time.sleep(delay)
            delay *= 2
            continue

        return resp.json()

    raise Exception("Max retries exceeded")


# -----------------------------
# AGENT REQUEST
# -----------------------------
def send_to_agent(prompt:Any) -> Dict[str, Any]:

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0,
    }

    response = post_with_retry(payload)

    content = response["choices"][0]["message"]["content"]

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        print("\nFailed to parse JSON. Raw output:\n", content)
        raise