import logging,requests
from aiogram import Bot, Dispatcher, executor, types
################################################################
#################################################################
headers = requests.utils.default_headers() #header
headers.update({'User-Agent': 'Mozilla/5.0 (X22; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
##########################################################
API_TOKEN = 'add token here'     #  <<<< ADD TOKEN HERE BRO
##########################################################
# Configure logging
logging.basicConfig(level=logging.INFO)
##########################################################
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
##########################################################
@dp.message_handler()
async def echo(message: types.Message):
    username = message.chat # this your username in telegram
    mtext = message.text # full url...
    ###########################################
        # code here :) FOR EXAMPLE HOW USE IT :)
    await message.answer("[+] user "+username)
    await message.answer("[+] Text "+mtext)
    ###########################################

##########################################################

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
