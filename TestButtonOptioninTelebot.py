import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
TELEGRAM_TOKEN = '1940813409:AAFcDNxju0PpzKxB4u-VHpDGAn6eH2c7VkQ'
bot = telebot.TeleBot(TELEGRAM_TOKEN)

#########################################################################
# Button
def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
    InlineKeyboardButton("Option 1", callback_data="cb_op1"),
    InlineKeyboardButton("Option 2", callback_data="cb_op2")
    )
    return markup
#########################################################################
# Handle Option using call.data .. exampe :cb_op1 .. 
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_op1":
        bot.answer_callback_query(call.id, "Choice Option 1")
    elif call.data == "cb_op2":
        bot.answer_callback_query(call.id, "Choice Option 2")
#########################################################################
@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, "Choice Option ???????", reply_markup=gen_markup())  #  Yes/No?
#########################################################################
bot.infinity_polling()
