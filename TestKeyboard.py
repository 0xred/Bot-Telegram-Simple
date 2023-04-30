# This example shows you how to create a custom QWERTY keyboard using reply keyboard markup
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "Token Here"
bot = telebot.TeleBot(TOKEN)

keys = ["Menu 1 op1","Menu 1 op2"]
symbols = ["Menu 2 op1","Menu 2 op2"]

def keyboard(key_type="Menu 1"):
    markup = ReplyKeyboardMarkup(row_width=10)
    if key_type == "Menu 1":
        row = [KeyboardButton(x) for x in keys[:10]]
        markup.add(*row)
        row = [KeyboardButton(x) for x in keys[10:20]]
        markup.add(*row)
        row = [KeyboardButton(x) for x in keys[20:29]]
        markup.add(*row)
        row = [KeyboardButton(x) for x in keys[29:]]
        markup.add(*row)
        markup.add(KeyboardButton("Menu 2"),KeyboardButton("✅Done"))
    elif key_type == "Menu 2":
        row = [KeyboardButton(x) for x in symbols[:10]]
        markup.add(*row)
        row = [KeyboardButton(x) for x in symbols[10:20]]
        markup.add(*row)
        row = [KeyboardButton(x) for x in symbols[20:]]
        markup.add(*row)
        markup.add(KeyboardButton("Menu 1"),KeyboardButton("✅Done"))
    else:
        row = [KeyboardButton(x.upper()) for x in keys[:10]]
        markup.add(*row)
        row = [KeyboardButton(x.upper()) for x in keys[10:20]]
        markup.add(*row)
        row = [KeyboardButton(x.upper()) for x in keys[20:29]]
        markup.add(*row)
        row = [KeyboardButton(x.upper()) for x in keys[29:]]
        markup.add(*row)
        markup.add(KeyboardButton("Menu 1"),KeyboardButton("Menu 2"),KeyboardButton("✅Done"))
    return markup

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id,"You can use the keyboard",reply_markup=keyboard())

@bot.message_handler(func=lambda message:True)
def all_messages(message):
    if message.text == "✅Done":
        markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id,"Finish Keyboard",reply_markup=markup)
    elif message.text == "Menu 2":
        bot.send_message(message.from_user.id,"This Menu 2",reply_markup=keyboard("Menu 2"))
    elif message.text == "Menu 1":
        bot.send_message(message.from_user.id,"This Menu 1",reply_markup=keyboard("Menu 1"))
    else:
        bot.send_message(message.chat.id,message.text)

bot.infinity_polling()
