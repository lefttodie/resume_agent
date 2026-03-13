import requests
import os

def extract_keywords(resume_text):

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}"
    }

    prompt = f"""
Extract 5 strong job search keywords from this resume.
Return only keywords separated by newline.

Resume:
{resume_text}
"""

    payload = {
        "model": "arcee-ai/trinity-large-preview:free",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    result = response.json()

    keywords = result["choices"][0]["message"]["content"]

    return keywords