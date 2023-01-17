import os
import telebot
import constants
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(constants.API_KEY)

keyboard = InlineKeyboardMarkup()
button1 = InlineKeyboardButton('🔰  خرید اشتراک  🔰', callback_data='option1')
button2 = InlineKeyboardButton('📝   پشتیبانی  📝', callback_data='option2')
button3 = InlineKeyboardButton('📜  آموزش‌ها', callback_data='option3')
button4 = InlineKeyboardButton('📊 حساب‌های من', callback_data='option4')
keyboard.add(button1, button2, button3, button4)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, World!')



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)



bot.polling()
