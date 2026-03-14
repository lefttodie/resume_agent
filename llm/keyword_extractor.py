import requests
import os
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def extract_keywords(resume_text):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
Extract 5 strong job search keywords from this resume.
Return only keywords separated by newline.

Resume:
{resume_text}
"""
    payload = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=payload)
    result = response.json()

    if "error" in result:
        raise ValueError(f"OpenRouter error: {result['error']}")
    if "choices" not in result:
        raise ValueError(f"OpenRouter response invalid: {result}")

    keywords = result["choices"][0]["message"]["content"]
    return [k.strip() for k in keywords.split("\n") if k.strip()]