import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

print("Loaded API KEY:", OPENROUTER_API_KEY)

url = "https://openrouter.ai/api/v1/embeddings"

headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "embedding-test"
}

payload = {
    "model": "text-embedding-3-small",
    "input": "Machine learning engineer with Python and NLP experience"
}

response = requests.post(url, headers=headers, json=payload)

print("Status Code:", response.status_code)
print("Response:", response.text)

if response.status_code == 200:
    embedding = response.json()["data"][0]["embedding"]
    print("Embedding length:", len(embedding))