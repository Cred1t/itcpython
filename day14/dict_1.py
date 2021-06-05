
# Наши Аккаунты в банках
accounts = [
    {
        "name": 'Demir Bank',
        "balance": 500000.00,
        "valuta": "KGS",
        "password": 1994
    },
    {
        "name": 'Optima Bank',
        "balance": 9654321,
        "valuta": "RUS",
        "password": 1995
    },
    {
        "name": 'KICB',
        "balance": 978423.15,
        "valuta": "USD",
        "password": 1996
    },
    {
        "name": 'Dos-Credo Bank',
        "balance": 75542.65,
        "valuta": "EUR",
        "password": 1997
    }
]
# Курс валют
curs = {
    "EUR": 101.65,
    "USD": 84.80,
    "RUS": 1.23,
    "KZT": 0.010
}
print('Мои аккаунты в банках:')
for index in range(len(accounts)):
    print(index + 1, accounts[index]['name'])
aindex = int(input('Выберите Аккаунт: '))
if aindex < 5 and aindex >= 1:
    rindex = aindex - 1
    print(accounts[rindex]['name'])
    pin = int(
        input('Введите PIN код: ')
    )
    if pin == accounts[rindex]['password']:
        print(
            'Добро пожаловать в', 
            accounts[rindex]['name']
        )
        print(
            'Ваш баланс: ', 
            accounts[rindex]['balance']
        )
    else:
        print('Вы не правильно вели PIN код')
else:
    print('Такой аккаунт нету в базе данных')