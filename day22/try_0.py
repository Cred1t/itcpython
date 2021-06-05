
try:
    a = int(input('Введите первое число: '))
    b = int(input('Введите разделитель числа: ')) 
    z = a / b
print(z)
except NameError:
    print('Ошибка: Неправильные переменные')
except IndentationError:
    print('Ошибка: Отступы в коде')
except ValueError:
    print('Ошибка: Текст не синтаксируется')
except ZeroDivisionError:
    print('Ошибка: делить на 0 нельзя ')
except:
    print('Ой ошибка')

print(2 / 0)