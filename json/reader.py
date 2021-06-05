
import json

user = {
    "name": "Нурбек",
    "age": 26,
    "birthDate": "02.06.2021",
    "city": "Osh"
}

user_json = open('users.json', 'w')
# Записать dict в файл
json.dump(user, user_json)


user_json = open('users.json', 'r')
# Прочитать json в файл
user_dict = json.load(user_json)
print(user_dict)