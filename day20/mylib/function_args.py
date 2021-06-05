
# Динамические получает параметры
# def sample(*args):
#     sum = 0
#     for a in args:
#         sum = sum + a
#         print(sum)

# sample(4, 5, 7864, 896, 986, 868686, 669669)

# def sample(**kwargs):
#     print(kwargs['name'])
#     print(kwargs['model'])
#     print(kwargs['weight'])
#     print(kwargs['god'])
#     print(kwargs['price'])

# sample(
#     name = 'Toyota',
#     model = 'Prius',
#     weight = '2400кг',
#     god = '2012 Года',
#     price = 'Окончательная цена 423 000сом'
# )

def my_pc(**kwargs):
    print(kwargs['processor'])
    print(kwargs['ghz'])
    print(kwargs['core'])
    print(kwargs['ssd'])
    print(kwargs['videocard'])
    print(kwargs['ram'])
    print(kwargs['model'])


my_pc(
    processor = 'Intel core i18+ 1111900K',
    ghz = '126.8 GHZ',
    core = '1 ТБ',
    ssd = '1000 ТБ',
    videocard = 'Gefors rtx 11080 Ti',
    ram = '10 ТБ',
    model = '-'
)