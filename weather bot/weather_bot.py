import requests
import datetime
from keys import open_weather_token, bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Hello, send me a city name')


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        resp = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric")
        data = resp.json()

        city = data['name']
        cur_weather = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        description = data['weather'][0]['main']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        day_lenght = sunset - sunrise

        #await message.reply()
        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                            f'City: {city}\ntemp: {cur_weather}C\n'
                            f'feels_like: {feels_like}\nhumidity: {humidity}\npressure: {pressure}\n'
                            f'wind: {wind}\n'
                            f'conditions: {description}\n'
                            f'sunrise :{sunrise}\nsunset: {sunset}\n'
                            f'day_lenght :{day_lenght}\n'
                            )

    except:
        await message.reply('\U00002620 check the city name')


if __name__ == '__main__':
    executor.start_polling(dp)
