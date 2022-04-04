from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/start')
b2 = KeyboardButton('/help')
b3 = KeyboardButton('/contacts')

kb_client = ReplyKeyboardMarkup()
kb_client.add(b1).add(b2).add(b3)