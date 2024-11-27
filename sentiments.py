import requests
import os


API_URL = "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base"
headers = {"Authorization": "Bearer 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"}


def sentiment_analysis(message):
  try:
    payload = {"inputs": message.text}
    response = requests.post(API_URL, headers=headers, json=payload)
    json = response.json()
    tone = json[0][0]['label']
    return f"This text has a tone of *{tone}*"
  except:
    return "Some error occurred"
