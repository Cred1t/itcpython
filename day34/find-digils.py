
import random

random_san = random.randint(1, 9)

while True: 
    print('Я загадаю чило от 1 до 9')
    num = int(input('Введи мое загаданное число: '))
    if num == random_san:
        print('Ураа ты угадал')
        break

    elif num > random_san:
        print('Вы вели большое число чем у рандома')

    elif num < random_san:
        print('Вы вели меньшее число чем у рандома')