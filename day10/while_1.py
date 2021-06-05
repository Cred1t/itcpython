
password = 1213
mepassword = 0
trycount = 5

while mepassword != password and trycount > 0:
    mepassword = int(input('Ваш пароль: '))
    if mepassword != password:
        trycount = trycount - 1
        print('У вас осталос', trycount, 'попыток')
        print('Не правильно')
    else:
        print('Ваш пароль верен Пока')



# sum = 1
# for i in range(100000000000000000000000000000000000000000000000000000000000):
#   if i % 2 != 0:
#     sum = sum * i
#     print(sum)