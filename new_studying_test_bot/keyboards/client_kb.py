from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/help')
b2 = KeyboardButton('/contacts')
b3 = KeyboardButton('/tours')
#b4 = KeyboardButton('/share number', request_contact=True)
#b5 = KeyboardButton('/share location', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#kb_client.add(b1).add(b2).insert(b3)
kb_client.add(b1).add(b2).insert(b3)#.row(b4, b5)