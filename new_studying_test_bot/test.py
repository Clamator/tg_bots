from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram import Bot, types

bot = Bot(token='5102696891:AAGsKx2cLvXsXosamo6eRbqC_dEbaFj0Ri0')
dp = Dispatcher(bot)

@dp.message_handler(lambda message: 'достав' in message.text)
async def order_delivery(message: types.Message):
    await message.answer('use this number to make an order +79999999999')

executor.start_polling(dp, skip_updates=True)
