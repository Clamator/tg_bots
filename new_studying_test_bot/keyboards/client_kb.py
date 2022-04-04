from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/help')
b2 = KeyboardButton('/contacts')
b3 = KeyboardButton('/tours')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#kb_client.add(b1).add(b2).insert(b3)
kb_client.row(b1, b2, b3)