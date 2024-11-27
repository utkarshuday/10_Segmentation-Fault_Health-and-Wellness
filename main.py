import requests
import telebot

BOT_TOKEN = "8010083364:AAHP1B1cLk7kL0a7eEx3zAzSomnCBD0zHYw"
API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
headers = {"Authorization": "Bearer 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"}

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
  bot.reply_to(message, "Hello autistic peeps, how can I help?")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
  text = sentiment_analysis(message)
  bot.reply_to(message, text)


def sentiment_analysis(message):
  payload = {"inputs": message.text}
  response = requests.post(API_URL, headers=headers, json=payload)
  return response.text


# text = "ngl, she has the gyatt"
# result = sentiment_analysis(text)
# print(result)


# def query(payload):
#   response = requests.post(API_URL, headers=headers, json=payload)
#   return response.json()

bot.infinity_polling()
