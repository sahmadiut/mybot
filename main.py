import os
import telebot
import constants

bot = telebot.TeleBot(constants.API_KEY)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, World!')

bot.polling()
