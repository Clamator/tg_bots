from aiogram.dispatcher.filters import Text

from new_studying_test_bot.create_bot import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher

ID = None

class FSMAdmin(StatesGroup):
    photo = State()
    location_name = State()
    description = State()
    tour_price = State()

#@dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def check_if_admin(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'what to do?') #, reply_markup=button_case_admin)
    await message.delete()

# main handler to add tour
#@dp.message_handler(commands='add_tour', state=None)
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('upload a photo')

#@dp.message_handler(state="*", commands=['cancel'])
#@dp.message_handler(Text(equals='cancel', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('ok')

# catch the 1st answer, write into the dict by id
#@dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def upload_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Enter location name')

# catch the 2nd answer
#dp.message_handler(state=FSMAdmin.location_name)
async def set_loc_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['location_name'] = message.text
        await FSMAdmin.next()
        await message.reply('Enter description')

# catch description
#dp.message_handler(state=FSMAdmin.description)
async def set_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply('Enter tour price ')

# catch tour price
#dp.message_handler(state=FSMAdmin.tour_price)
async def set_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['tour_price'] = float(message.text)

        async with state.proxy() as data:
            await message.reply(str(data))

        await state.finish()


# reg handlers
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['upload_photo'], state=None)
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(check_if_admin, commands=['moderator'], is_chat_admin=True)
    dp.register_message_handler(upload_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(set_loc_name, state=FSMAdmin.location_name)
    dp.register_message_handler(set_description, state=FSMAdmin.description)
    dp.register_message_handler(set_price, state=FSMAdmin.tour_price)
    dp.register_message_handler(cancel_handler, state="*", commands=['cancel'])



