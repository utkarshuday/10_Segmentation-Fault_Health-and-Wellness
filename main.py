import os
import telebot

from dotenv import load_dotenv
from sentiments import sentiment_analysis

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_intro(message):
  bot.reply_to(
      message,
      "Hello! 👋 I'm a Bot to help you communicate.\n"
      "I can help identify the tone of a conversation and reply appropriately.\n"
      "For example, I might detect if a message is positive, negative, or neutral.\n\n"
      "Start exploring! 😊"
  )


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
  text = sentiment_analysis(message)
  bot.reply_to(message, text)


bot.infinity_polling()
