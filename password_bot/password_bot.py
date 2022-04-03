from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random


bot_token = '5151485113:AAHyjSV-H_aKAe5MM8pSz-GhGjGPQlu5ybE'
bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Hello, it is a bot to create a password for any cases. Enter a length of password')


@dp.message_handler()
async def gen_password(message: types.Message):
    try:
        pas = ''
        for x in range(int(message.text)):
            pas = pas + random.choice(
                list('+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'))
        await message.reply(pas)
    except:
        await message.reply('enter a integer')


if __name__ == '__main__':
    executor.start_polling(dp)
