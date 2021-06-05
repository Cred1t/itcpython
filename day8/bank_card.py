predator_sena = 3500
balance = 5000
summa = int(input('Введите сумму: '))

print('Чтобы купить Acer Predator за 3500$: ')
sposob = (input('Введите способ оплаты: ')).lower()

if sposob == 'mastercard':
    print('Извините мы не поддерживаем Mastercard')
elif sposob == 'elcard':
    print('Извините мы не поддерживаем Elcard')
elif sposob == 'visa' or sposob == 'paypal':
    creditcard = input('Введите номер вашей карты: ')

    if len(creditcard) > 4 or len(creditcard) < 4:
        print('Некорректный номер карты ')
        quit()

    if predator_sena > balance:
        print('У вас не достаточно средств')
else: 
    print('Вы можете совершить покупку')
    print('Поздравляем вы преоблели Acer Predator')
    print('Остаток', balance - summa)
else: 
    print('Такой вид карты не поддерживается')
# cridcart = input('Введиете номер вашей карты: ')
