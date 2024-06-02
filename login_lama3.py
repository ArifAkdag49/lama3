from huggingface_hub import login
import os

# Hugging Face API tokenini çevresel değişkenden alın
token = os.getenv("HUGGINGFACE_TOKEN")

# Tokeni kullanarak giriş yapın
login(token)
