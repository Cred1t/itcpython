number1 = int(input('1 дайте число: '))
number2 = int(input('2 дайте число: '))

symbol = input('Какое действие предпочитаете: ')

# print(number1, symbol, number2, '= ?')

if symbol == '+' or symbol == '-':
    print(number1 + number2)
if symbol == '-':
    print(number1 - number2)
if symbol == '*':
    print(number1 * number2)
if symbol == '/':
    print(number1 / number2)
if symbol == '**':
    print(number1 ** number2)
else
    print('Нельзя делить на ноль')