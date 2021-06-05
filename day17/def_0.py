
# Функция это блок операторов которые можно вызвать где угодно
# def summa(num1, num2):
#     print('----------') 
#     print('Сумма: {}'.format(san1 + san2))  
#     print('----------')

# def mines(num1, num2):
#     print('----------') 
#     print('Сумма: {}'.format(san1 - san2))  
#     print('----------')

# san1 = int(input('Число 1: '))
# san2 = int(input('Число 2: '))

# summa(san1, san2)
# mines(san1, san2)


# def salam_en():
#     print('Hello Hi How are You')
#     print('Maybe go to learn Python')

# def salam_ru():
#     print('Здраствуйте. Как дела? ')
#     print('Пошлите учить Python')
# lang = input('На каком языке вас приветствовать: ')

# if lang == 'en':
#     salam_en()
# elif lang == 'ru':
#     salam_ru()


def salamdash(lang):
    if lang == 'en':
        print('Hello Hi How are You')
        print('Maybe go to learn Python')
    elif lang == 'ru':
        print('Добрый вечер')
        print('Поехали учить Python')
    elif lang == 'kg':
        print('Ассалом Алейкум. Иштер кандай? ')
        print('Pyhton уйронгону кеттикби')
    

# l = input('На каком языке с вами поприветсвоваться: ')
salamdash('en')