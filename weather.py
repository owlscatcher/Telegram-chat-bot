import requests
import json
from datetime import datetime
from search_city import Get_city
import security


def Get_Weather(city):
    api_key = security.api_key.get(security.OPEN_WEATHER_MAP_KEY)
    lang = 'RU'

    id = Get_city(city)

    if id == None or id == '':
        return 'Город не найден...'

    url = f'http://api.openweathermap.org/data/2.5/forecast?id={id}&lang={lang}&units=metric&appid={api_key}'

    response = requests.get(url)
    parse_dict = response.json()

    day = parse_dict.get('list')

    day_date = None
    return_text = city + ':'

    icon_dict = {'01d': '☀️',
                 '02d': '⛅️',
                 '03d': '☁️',
                 '04d': '☁️',
                 '09d': '💦',
                 '10d': '💧',
                 '11d': '⚡️',
                 '13d': '❄️',
                 '50d': '🌫',
                 '01n': '🌑',
                 '02n': '⛅️',
                 '03n': '☁️',
                 '04n': '☁️',
                 '09n': '💦',
                 '10n': '💧',
                 '11n': '⚡️',
                 '13n': '❄️',
                 '50n': '🌫'}

    for d in day:
        dt = d.get('dt_txt')
        temp = d.get('main').get('temp')
        feels_like = d.get('main').get('feels_like')
        weather = d.get('weather')[0].get('description')
        icon = d.get('weather')[0].get('icon')

        data = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
        if (str(data.time()) == '06:00:00' or str(data.time()) == '12:00:00' or str(data.time()) == '18:00:00' or str(data.time()) == '00:00:00'):
            if day_date != data.date():
                day_date = data.date()
                return_text += '\n\n[' + str(day_date) + ']:'
            return_text += '\n[' + str(data.time())[:5] + ']: ' + icon_dict.get(icon) + ', ' + \
                str(temp) + '℃  (ощущ. как ' + str(feels_like) + '℃ )'

    return return_text
