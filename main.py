import os
import telebot
import constants
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

bot = telebot.TeleBot(constants.API_KEY)


keyboard = InlineKeyboardMarkup()
button1 = InlineKeyboardButton('🔰  خرید اشتراک  🔰', callback_data='a')
button2 = InlineKeyboardButton('📝   پشتیبانی  📝', url='https://t.me/sajjad_ahmadi_sh')
button3 = InlineKeyboardButton('📜  آموزش‌ها', callback_data='b')
button4 = InlineKeyboardButton('📊 حساب‌های من', callback_data='c')
keyboard.add(button2, button3, button4, button1)



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'سلام.\n'
                                      'به فروشگاه vpn پرسرعت V2ray خوش آمدید.\n'
                                      'برای استفاده از اطلاع‌رسانی‌ها و مطالب آموزنده، لطفا در کانال ما ( @vi2ray ) عضو شوید.\n', reply_markup=keyboard)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


# list of commands
# use in for delete with the necessary scope and language_code if necessary
bot.delete_my_commands(scope=None, language_code=None)

bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("/start", "منوی اصلی"),
    ],
)

# check command
cmd = bot.get_my_commands(scope=None, language_code=None)
print([c.to_json() for c in cmd])


bot.polling()
