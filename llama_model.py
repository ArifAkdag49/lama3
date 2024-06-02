import requests

# Hugging Face API URL ve token
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
headers = {"Authorization": f"Bearer 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"}

def generate_response(prompt):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}
