from aiogram import Bot, Dispatcher, types, executor
from asyncio import sleep
###########################################################
API_TOKEN = 'Token here bro' 
MYBOT = Bot(API_TOKEN)
dp = Dispatcher(MYBOT)
###########################################################
# /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	username = message.from_user.username
	msg = f"<b>Hello</b>, <i>{username}!</i>\n For Help use /help "
	await MYBOT.send_message(message.chat.id, msg, parse_mode='html')
###########################################################
# /whoami
@dp.message_handler(commands=['whoami'])
async def whoami(message: types.Message):
	username = message.from_user.username
	id = message.from_user.id
	whoami_msg = f"username: {username}\nid: {id}"
	await MYBOT.send_message(message.chat.id, whoami_msg)
###########################################################
# /help
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
	text_help = f'/start - Start \n' \
	            f'/whoami - Show Username and id \n' \
	            f'/help - Just For Help \n' \
	            f'/ask - just ask bot i dont have answer lol\n' 
	await MYBOT.send_message(message.chat.id, text_help, parse_mode='html')
###########################################################
# /ask <<<< this for you ,, try write like /start /whoami /help ... it is easy
###########################################################

if __name__ == '__main__':
	executor.start_polling(dp, loop=True)

