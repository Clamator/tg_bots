from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_load = KeyboardButton('/upload_photo')
button_delete = KeyboardButton('/delete')

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_delete)