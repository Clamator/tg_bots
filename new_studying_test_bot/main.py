from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


# client
@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Shalom Aleychum')
        #await message.delete()
    except:
        await message.reply('Communicating with bot is available only via private messages. t.me/new_studying_test_bot')


@dp.message_handler(commands=['contacts'])
async def show_contacts(message: types.Message):
    await bot.send_message(message.from_user.id, 'Moscow, Red Square, 1, +79999999999, mon-fr, 8:00-20:00', disable_web_page_preview=True,
                           protect_content=True, allow_sending_without_reply=False)




@dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer('pidor')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
