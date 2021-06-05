
cars = {
    'Toyota': 1999,
    'Hyndai': 2006,
    'Kia': 2008
}

try:
    car_file = open('cars.txt', 'w')
    for key, value in cars.items():
        car_file.writelines(key + ',' +str(value) + '\n')
    # text = 'Merssedes, 1943'
    # car_file.writelines(text)

except FileNotFoundError:
    print('Ошибка: Указанный файл не найден')