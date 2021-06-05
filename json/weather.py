
import json
import requests
weather_api_url = 'https://goweather.herokuapp.com/weather/'
city = input('Введите имя города чтобы узнать погоду: ')
req = requests.get(weather_api_url + city)
data = req.json()
print('Погода в ' + city + ': ', end='')
print(data['temperature'])
print('Погода: ' + city + ': ')
print(data['description'])