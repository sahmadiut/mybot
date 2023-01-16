import os
import telebot
import constants

bot = telebot.TeleBot(constants.API_KEY)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, World!')


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.polling()
