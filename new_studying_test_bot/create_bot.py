from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

#bot = Bot(token=os.getenv('TOKEN'))
bot = Bot(token='5102696891:AAGsKx2cLvXsXosamo6eRbqC_dEbaFj0Ri0')
dp = Dispatcher(bot, storage=storage)
