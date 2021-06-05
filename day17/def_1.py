def calculator(num1, num2, suff):
    if suff == '*':
        print(num1 * sum2)
    elif suff == '/':
        print(num1 / num2)
    elif suff == '**':
        print(num1 ** num2)
    elif suff == '+':
        print(num1 + num2)
    elif suff == '-':
        print(num1 - num2)

num1 = int(input('Число 1: '))
num2 = int(input('Число 2: '))
a = input('Какое действие предпочитаете: ')
calculator(num1, num2, a)