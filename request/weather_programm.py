
import requests

api_key = 'fa0c69065a227aae0ae1081d5953bcfa'
site = 'https://api.openweathermap.org/data/2.5/weather?q={city},{state}&appid={api_key}&units=metric'
city = input('Введите ваш город: ')
state = input('Введите код страны: ')
site = site.format(city = city, state = state, api_key=api_key)
data  = requests.get(site)
data_dict = data.json()
print('Погода в', city, state)
print(data_dict['main']['temp'], 'градусов')
print('Ощущается:', data_dict['main']['feels_like'], 'градусов')
if data_dict['weather'][0]['main'] == 'Clouds':
    print('Погода в', city, 'Облачно')
if data_dict['weather'][0]['main'] == 'Clear':
    print('Погода в', city, 'Ясно')