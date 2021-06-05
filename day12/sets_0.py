
# names = {'Amantyr','Amantyr','Emir', 'Erlan','Emir', 'Zalkar'}

# print(names)



# emails = [
#     'zalkar@gmail.com '
#     'amantyr@gmail.com '
#     'erlan@gmail.com '
#     'emir@gmail.com '
#     'amantyr@gmail.com '
#     'zalkar@gmail.com '
#     'emir@gmail.com '
#     'amantyr@gmail.com '
# ]

# emails = set(emails) 
# {'zalkar@gmail.com', 'amantyr@gmail.com', ...}
# for email in emails:
#     print('На почту', email, 'отправлен приглашение на вечеринку')



# products = {
#     'сахар'
# }
# print(products)

# products.add('чай')
# products.add('соль')



# products = {'сахар'}

# product = ''
# for i in range(5):
#     product = input('Продукт на продаже: ')
#     products.add(product.lower())

# print(products)



# products = {
#     'Сахар '
#     'Чай '
#     'Нан '
#     'Суу '
#     'Макарон '
# }

# fruits = {
#     'apple',
#     'watermelon'
# }

# print('До: ', products)

# products.update(fruits)

# print('После удаление: ', products)



# company1 = { 'apple', 'microsoft', 'kia', 'honda' }
# company2 = { 'LG', 'panasonic', 'microsoft', 'apple'}
# company3 = { 'Sonny', 'Toyota', 'BMW' }

# # difference_company = company1.difference(company2)
# # print(company1.difference(company2)) 

# # intersection = company1.intersection(company2)
# # print(intersection)

# company1.intersection_update(company2)
# print(company1)
# company1.intersection_update(company3)
# print(company1)



# company1 = { 
#     'apple',
#     'microsoft',
#     'kia',
#     'honda'
# }
# company1.pop()
# print(company1)



users = { 
    'Залкарбек',
    'Зарлык',
    'Амантур',
    'Tima',
    'Том',
    'Mike',
    'John',
    'Rik',
    'Krishna',
    'Jobs',
    'Бекзат',
    'Steve',
    'Rocki',
    'Бекгазы'
}

prizmesto = int(input('Введите количество призовых мест: '))

for i in range(prizmesto):
    print(i + 1, 'место',users.pop())