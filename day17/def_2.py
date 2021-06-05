
def progress(num):
    geo = 1
    text = ''
    for i in range(1, num + 1):
        geo = geo * i
        if i == num:
            text = text + '{} = '.format(i)
        else:
            text = text + '{} * '.format(i)
    print('Ответ:', text, geo)
g = int(
    input('Задайте число 1: ')
)
g2 = int(
    input('Задайте число 2: ')
)
progress(g)
progress(g2)

# for i in range(1, 1000000000):
#     print(i)