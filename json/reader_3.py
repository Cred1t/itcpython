
import json 

file = open('countries_2.json', 'r')
countries = json.load(file)

while True:
    name = input('Введиет имя страны: ')

    if name == 'exit':
        break
    for country in countries: 
        if country['country'] == name:
            print(country['calling_code'])