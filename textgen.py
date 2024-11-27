import requests

RESPONSE_MODEL = "google/flan-t5-large"

# Hugging Face Inference API endpoint for response generation
RESPONSE_API_URL = f"https://api-inference.huggingface.co/models/{
    RESPONSE_MODEL}"

# Headers for authentication
headers = {
    "Authorization": "Bearer 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"
}

# Function to generate a response based on the provided sentiment analysis data


def generate_dynamic_response(input_text, emotions):
  # Get the dominant emotion (the one with the highest score)
  primary_emotion = max(emotions, key=lambda x: x["score"])["label"]

  # Customize the response generation prompt dynamically based on the detected emotion
  user_prompt = f"""Respond in an {
      primary_emotion} tone. {input_text}"""

  # Generate response using Hugging Face model
  payload = {
      "inputs": user_prompt,
      "parameters": {
          "max_length": 100,
          "num_return_sequences": 1,
          "temperature": 0.7,
          "top_p": 0.9
      }
  }
  response = requests.post(RESPONSE_API_URL, headers=headers, json=payload)

  if response.status_code == 200:
    return response.json()[0]["generated_text"]
  else:
    return f"Error: {response.status_code}, {response.text}"


# Example usage with a pre-defined emotion analysis result
if __name__ == '__main__':
  # Sample emotion analysis data
  emotions = [
      {"label": "anger", "score": 0.02},
      {"label": "disgust", "score": 0.9},
      {"label": "fear", "score": 0.01},
      {"label": "joy", "score": 0.04},
      {"label": "neutral", "score": 0.04},
      {"label": "sadness", "score": 0.02},
      {"label": "surprise", "score": 0.02}
  ]

  # Sample user input
  input_text = "I'm overwhelmed by the variety of options."

  # Generate dynamic response based on the emotion analysis data
  reply = generate_dynamic_response(input_text, emotions)
  print(f"AI Reply: {reply}")
