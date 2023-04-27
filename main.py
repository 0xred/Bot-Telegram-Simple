from aiogram import Bot, Dispatcher, types, executor
import openai

###########################################################
API_TOKEN = 'Token telegram' 
openai.api_key = "Token Openai"
MYBOT = Bot(API_TOKEN)
dp = Dispatcher(MYBOT)
###########################################################
# /start
@dp.message_handler(commands=['start'])
async def help(message: types.Message):
	await MYBOT.send_message('[+] Bot GPT By RedShadow @WTTTF')
###########################################################
@dp.message_handler() # For any text in chat : Your Ask Ai
async def echo(message: types.Message):
	mytext = message.text 
	response = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages=[{"role":"user","content": mytext}]
		)
	aichat = response.choices[0].message.content 
	await message.answer(aichat) # Answer Ai
###########################################################
if __name__ == '__main__':
	executor.start_polling(dp, loop=True)
