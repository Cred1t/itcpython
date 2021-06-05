
import json

file = open('countries.json', 'w')
c = []
while True:
    country = {}
    name = input('Введите имя страны или exit для выхода из программы: ')

    if name == 'exit':
        break

    valuta = input('Введите Валюту или exit для выхода из программы: ')

    if valuta == 'exit':
        break

    country['name'] = name
    country['valuta'] = valuta

    c.append(country)

# Мамлекеттердин списогун countries.json файлына жазгыла
json.dump(c, file)