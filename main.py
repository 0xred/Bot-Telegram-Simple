from aiogram import Bot, Dispatcher, types, executor
from asyncio import sleep
import openai

###########################################################
API_TOKEN = 'Token Telegram Bot Here' 
MYBOT = Bot(API_TOKEN)
dp = Dispatcher(MYBOT)
###########################################################
# /help
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
	await MYBOT.send_message('[+] Bot GPT By RedShadow @WTTTF')
###########################################################
@dp.message_handler() # For any text in chat >> YOUR ASK
async def echo(message: types.Message):
	mytext = message.text 
	openai.api_key = "TOKEN Openai API Here"
	response = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages=[{"role":"user","content": mytext}]
		)
	aichat = response.choices[0].message.content ###
	await MYBOT.send_message(aichat)
###########################################################
if __name__ == '__main__':
	executor.start_polling(dp, loop=True)
