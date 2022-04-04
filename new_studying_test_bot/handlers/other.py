from aiogram import types, Dispatcher
from new_studying_test_bot.create_bot import dp



#@dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer('pidor')

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)