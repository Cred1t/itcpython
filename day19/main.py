
# import module_0
# phone = input('Введите номер телефона: ')
# module_0.check_phone_number(phone)

# import module_0
# module_0.translate()

# fio = module_0.getFullName('Амантур', 'Торогулов') 
# print(fio)

# import mylib.calc.calculator as calculate



# import random

# rstart = int(input('Введите начала рандома: '))
# rend = int(input('Введите конец рандома: '))

# print('Рандомное число: ', random.randint(rstart, rend))



import random 

mynum = int(input('Загадайте одно число, я попробую найти это число через функцию ranint: '))

choose_num = random.randint(1, mynum + 10)

while choose_num != mynum:
    choose_num = random.randint(1, mynum + 10)
    print('Это твое число? ', choose_num)

if choose_num == mynum:
    print('Я нашел твое число ', choose_num)