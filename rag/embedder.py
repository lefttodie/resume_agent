import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def create_embeddings(chunks):
    
    url = "https://openrouter.ai/api/v1/embeddings"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "resume-agent"
    }

    payload = {
        "model": "text-embedding-3-small",
        "input": chunks
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Embedding error: {response.text}")

    data = response.json()

    embeddings = [item["embedding"] for item in data["data"]]

    return embeddings