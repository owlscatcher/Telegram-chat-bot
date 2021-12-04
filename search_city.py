import requests

def Get_city(city):
    jQuery = 'jQuery19107507303002785439_1596333497062'
    url = f'https://openweathermap.org/data/2.5/find?callback={jQuery}&q={city}&type=like&sort=population&cnt=30&appid=439d4b804bc8187953eb36d2a8c26a02&_=1596333497064'

    responce = requests.post(url)

    responce = responce.text[responce.text.find('id'):]
    responce = responce[:responce.find(',')]
    responce = responce[responce.find(':')+1:]

    return responce
