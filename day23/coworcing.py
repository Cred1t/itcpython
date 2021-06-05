
# -------------------------------------------------------------------
# Задача 1
# -------------------------------------------------------------------

# names = {
#     'Руслан' : 26,
#     'Кадыр' : 23,
#     'Ерлан' : 22
# }
# try:
#     name_file = open('vw.txt', 'w')
#     for key, value in names.items():
#         name_file.writelines(key + ',' +str(value) + '\n')


# except FileNotFoundError:
#     print('u dont have such a module or file!')

# ---------------------------------------------------------------------
# Задача 2
# ---------------------------------------------------------------------

# a = input('Введите ваше полное ФИО: ')
# if "уулу" in a or "кызы" in a:
#     s = a.split()
#     print(f"last name: {s[0]} {s[1]},  first name: {s[2]}")

# else:
#     s = a.split()
#     print(f"first name: {s[-1]}  last name: {s[0]}")

# ---------------------------------------------------------------------
# Задача 3 
# ---------------------------------------------------------------------

# tasks_file = open('tasks.txt', 'r')

# tasks_list = tasks_file.readlines()

# for task in tasks_list:
#     t = task.strip()
#     print(t, '=', eval(t))