# from huggingface_hub import login
# import os

# # Hugging Face API tokenini çevresel değişkenden alın
# token = os.getenv("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")

# # Tokeni kullanarak giriş yapın
# login(token)



from huggingface_hub import login

# Yeni oluşturduğunuz token'ı buraya ekleyin
token = "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"

try:
    login(token)
    print("Successfully logged in!")
except ValueError as e:
    print(f"Failed to log in: {e}")




