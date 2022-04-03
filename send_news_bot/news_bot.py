import time
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from bs4 import BeautifulSoup
import schedule
from aiogram.types.poll import *


bot_token = '5128669020:AAHuwpF40rUMR_vnzJ4_U5wnwvfVuWnSZA0'
bot = Bot(token=bot_token)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply(
        'Hello, it is a bot to send news from different sites. For now it is habr.com/ru. Type anything to start bot sending news once a five minutes.')


@dp.message_handler()
async def parse_and_send_link(message: types.Message):
    news_lst = []
    while True:
        url = 'https://habr.com/ru/all/'
        try:
            if len(news_lst) > 5:
                news_lst = []
            resp = requests.get(url)
            soup = BeautifulSoup(resp.text, 'lxml')
            main_table = soup.find('div', class_='tm-articles-subpage').find('div', class_='tm-articles-list').find_all(
                'article', class_='tm-articles-list__item')
            first_new = main_table[0].find('h2', class_='tm-article-snippet__title tm-article-snippet__title_h2').find(
                'a').get('href')
            if first_new not in news_lst:
                await message.reply(f'https://habr.com{first_new}')
                news_lst.append(first_new)
                print(first_new)
                time.sleep(300)
            else:
                await message.reply('no unread news found')
                time.sleep(300)
        except:
            await message.reply('no unread news found')
            time.sleep(300)


#@dp.message_handler(commands=['stop'])
#async def stop_polling(message: types.Message):
#    pass


if __name__ == '__main__':
    executor.start_polling(dp)
