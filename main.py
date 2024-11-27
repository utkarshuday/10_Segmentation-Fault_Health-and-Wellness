import os
import requests
import telebot

from dotenv import load_dotenv, dotenv_values
load_dotenv()

BOT_TOKEN = (os.getenv("BOT_TOKEN"))
API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
headers = {"Authorization": f"Bearer {os.getenv("HUGGING_FACE_TOKEN")}"}

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
