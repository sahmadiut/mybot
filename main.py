import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot('5759504782:AAEUP8o8Dr50xGaFThzO7Q4-iBbKHseWYu8')

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, World!')

bot.polling()
