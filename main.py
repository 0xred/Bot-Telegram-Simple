from aiogram import Bot, Dispatcher, types, executor
from asyncio import sleep
###########################################################
API_TOKEN = 'Token here bro' 
MYBOT = Bot(API_TOKEN)
dp = Dispatcher(MYBOT)
###########################################################
# /help
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
	text_help = f'/help - For Help \n' \
	            f'/ask -  example /ask 2+2?\n' 
	await MYBOT.send_message(message.chat.id, text_help, parse_mode='html')
###########################################################
# /ask
@dp.message_handler(commands=['ask'])
async def help(message: types.Message):
	xtext = message.text 
	await MYBOT.send_message('[+] your ask about: '+xtext)
###########################################################
@dp.message_handler() # For any text in chat
async def echo(message: types.Message):
    await message.answer('[+] Wellcome To RedShadow Bot :) use /help') 
###########################################################
if __name__ == '__main__':
	executor.start_polling(dp, loop=True)
	
