
#programma bankomat DemirBank
correct_pin = 1203
balance_1 = 5000
nominals = [100, 200, 500, 1000, 2000, 5000]

print('Добро пожаловать Demir bank')
pin = int(input('Введите пин-код: '))

#Проверка PIN-кода на правильность 
if pin == correct_pin:
    print('1.Проверка баланса ') 
    print('2.Снятие ')
    print('3.Поменять пин-код ')
    print('4.Курс обмена ')
    operation = int(input('Выберите операцию: '))

    if operation == 1: 
        print('vash balance',balance_1)
        print('Ваш баланс в $', balance_1 / 84)
        print('Ваш баланс в €', balance_1 / 102)

    #Проверяем выбрали ли мы 2 операцию 
    if operation == 2:
        print(nominals)
        nominals = int(input('Сколько вы хотите снять?: '))
        balance_1 = balance_1 - nominals
        print('На вашем балансе осталось',balance_1)


    if operation == 3:
        parol = input('Хотите сменить пароль?: [Y/N] ')
        
        if parol == 'y':
            newpin = int(input('Введите новый пароль: '))
            verifi_pin = int(input('Введите PIN еще раз для проверки: '))
            print('Вы успешно сменили пароль!')
            
            
            if newpin != verifi_pin:
                print('Ошибка PIN')


            

        if parol == 'нет':
            quit()

    if operation == 4:
        print('$1 - 84,79 ')
        print('€1 - 102,22')
        print('₽1 - 1,13 ')
        

else:
    print('Неверный PIN-код!!!')


