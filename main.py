import os
import telebot
import constants
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

bot = telebot.TeleBot(constants.API_KEY)


keyboard = InlineKeyboardMarkup()
button1 = InlineKeyboardButton('🔰  خرید اشتراک  🔰', callback_data='🔰  خرید اشتراک  🔰')
button2 = InlineKeyboardButton('📝   پشتیبانی  📝', callback_data='📝   پشتیبانی  📝')
button3 = InlineKeyboardButton('📜  آموزش‌ها', callback_data='📜  آموزش‌ها')
button4 = InlineKeyboardButton('📊 حساب‌های من', callback_data='📊 حساب‌های من')
keyboard.add(button1, button2, button3, button4)


keyboard2 = InlineKeyboardMarkup()
chanelbutton = InlineKeyboardButton('🔰  عضویت در کانال  🔰', url='https://t.me/vi2ray')
checkButton = InlineKeyboardButton('تایید عضویت  ✅', callback_data='/start')
keyboard2.add(chanelbutton, checkButton)

# check if the user is member of the channel
def is_member(user_id):
    channel_id = constants.CHANNEL_ID
    try:
        channel_member = bot.get_chat_member(channel_id, user_id)
        if channel_member.status == 'member' or channel_member.status == 'creator' or channel_member.status == 'administrator':
            return True
        else:
            return False
    except:
        return False


def member_only(message):
    if not is_member(message.from_user.id):
        bot.send_message(message.chat.id, 'برای استفاده از ربات باید عضو کانال ما باشید.', reply_markup=keyboard2)
        return False
    else:
        return True


@bot.message_handler(commands=['start'])
def start(message):
    if member_only(message):
        bot.send_message(message.chat.id, 'به ربات خرید اشتراک وی‌پی‌آری خوش‌آمدید.', reply_markup=keyboard)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'option1':
            bot.send_message(call.message.chat.id, 'option1')
        elif call.data == 'option2':
            bot.send_message(call.message.chat.id, 'option2')
        elif call.data == 'option3':
            bot.send_message(call.message.chat.id, 'option3')
        elif call.data == 'option4':
            bot.send_message(call.message.chat.id, 'option4')



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)



bot.polling()
