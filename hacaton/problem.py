
# Problem 1
# ------------------------------------

# from datetime import datetime

# time  = 1544832000
# objects = datetime.fromtimestamp(time)

# print("datetime =", objects)

# ------------------------------------

# Problem 2

# ------------------------------------

# import json

# file = open('books.json', 'r')
# book = json.load(file)

# for i in book:
#     print('Заголовок: ')
#     print('Автор: ')
#     print('Страницы: ')
#     print('Дата выхода: ')
#     print()

# ------------------------------------

# Problem 3

# ------------------------------------

import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.0.117",
  user="group2",
  password="1",
  database = 'itc_group_2'
)

tododb = mydb.cursor()


while True:
    todo = input('введите задачу: ')
    sql = "INSERT INTO todos(todo) VALUES('{}')".format(todo)
    if todo == 'exit':
        break

    print(sql)
