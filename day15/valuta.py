
# Курс валют
curs = {
    "EUR": 101.65,
    "USD": 84.80,
    "RUS": 1.23,
    "KZT": 0.020
}

valuta = input('На какую валюту перевести средства: ')
money = float(
    input('Введите сумму: ')
)

if curs.get(valuta) != None:
    print(valuta, ':', money / curs[valuta])
else:
    print('Такой тип валюты не поддерживается')