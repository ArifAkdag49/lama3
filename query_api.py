import requests

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Örnek bir soru sorma
data = query({"inputs": "Hello, how are you?"})
print(data)
