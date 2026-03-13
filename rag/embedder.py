import requests
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def create_embeddings(text_chunks):

    embeddings = []

    url = "https://openrouter.ai/api/v1/embeddings"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}"
    }

    for chunk in text_chunks:

        payload = {
            "model": "text-embedding-3-small",
            "input": chunk
        }

        response = requests.post(url, headers=headers, json=payload)

        vector = response.json()["data"][0]["embedding"]

        embeddings.append(vector)

    return embeddings