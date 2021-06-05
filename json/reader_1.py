
import json
person = {}

login = input('Введите логин: ')
name = input('Введите имя: ')
phone_number = input('Введите телефон: ')

person['login'] = login
person['name'] = name
person['phone_number'] = phone_number

person_file = open('person.json', 'w')
json.dump(person, person_file)

person_file = open('person.json', 'r')
person = json.load(person_file)

person['language'] = input('Ваш язык: ')

person_file = open('person.json', 'w')
json.dump(person, person_file)