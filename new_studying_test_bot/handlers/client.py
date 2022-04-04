from aiogram import types, Dispatcher
from new_studying_test_bot.create_bot import dp, bot
from new_studying_test_bot.keyboards import kb_client

#@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Shalom Aleychum', reply_markup=kb_client)
        #await message.delete()
    except:
        await message.reply('Communicating with bot is available only via private messages. t.me/new_studying_test_bot')

#@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'you have pressed a Help button')
        #await message.delete()
    except:
        await message.reply('Communicating with bot is available only via private messages. t.me/new_studying_test_bot')

#@dp.message_handler(commands=['contacts'])
async def show_contacts(message: types.Message):
    await bot.send_message(message.from_user.id, 'Moscow, Red Square, 1, +79999999999, mon-fr, 8:00-20:00', disable_web_page_preview=True,
                           protect_content=True, allow_sending_without_reply=False)

async def show_tours(message: types.Message):
    await bot.send_message(message.from_user.id, 'no available tours yet', disable_web_page_preview=True,
                           protect_content=True, allow_sending_without_reply=False)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(show_contacts, commands=['contacts'])
    dp.register_message_handler(show_tours, commands=['tours'])
