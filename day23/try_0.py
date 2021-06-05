
tasks_file = open('tasks.txt', 'r')

tasks_list = tasks_file.readlines()

for task in tasks_list:
    try:
        t = task.strip()
        print(t, '=', eval(t))
    except ZeroDivisionError:
        print('Ошибка: Сбой в синтаксировании выражения')
    except FileNotFoundError:
        print('Ошибка: Файл не найден')
    except:
        print('Ошибка: Вернитесь в основную страницу')
