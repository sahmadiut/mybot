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


# use in for delete with the necessary scope and language_code if necessary
bot.delete_my_commands(scope=None, language_code=None)

bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("command1", "command1 description"),
        telebot.types.BotCommand("command2", "command2 description")
    ],
    # scope=telebot.types.BotCommandScopeChat(12345678)  # use for personal command for users
    # scope=telebot.types.BotCommandScopeAllPrivateChats()  # use for all private chats
)

# check command
cmd = bot.get_my_commands(scope=None, language_code=None)
print([c.to_json() for c in cmd])


bot.polling()
