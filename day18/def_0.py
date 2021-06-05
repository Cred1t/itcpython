
# def my_function(name, number):
#     print('World', name)
#     print('Country')
#     print('Great Jobs')
#     name = name + ' REPUBLIC'
#     print(name, '\n')
#     if number < 0:
#         print('Дай десятое число')
#     else:
#         number = number * number
#         print(number)

# my_function(-7)



def kvadrat(number):
    if number < 0:
        print('Дай десятое число')
    else:
        number = number * number
        print(number)

def divide(number1, number2):
    if number2 == 0:
        print('Нельзя делить на ноль')
    else:
        print(number1 / number2)

divide(10, 0)
