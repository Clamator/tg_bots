import datetime
import requests
from keys import open_weather_token
from pprint import pprint


def get_weather(city, token):
    try:
        resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric')
        data = resp.json()
        #pprint(data)


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

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***")
        print(f'City: {city}\ntemp: {cur_weather}C\n'
              f'feels_like: {feels_like}\nhumidity: {humidity}\npressure: {pressure}\n'
              f'wind: {wind}\n'
              f'conditions: {description}\n'
              f'sunrise :{sunrise}\nsunset: {sunset}\n'
              f'day_lenght :{day_lenght}\n'
              )

    except Exception as ex:
        print(ex, 'check the city name')

def main():
    city = input('enter a city name: ')
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()