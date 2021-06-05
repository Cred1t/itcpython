
def kz():
    print('Salem')

def ru():
    print('Привет')

def kg():
    print('Ассалом Алейкум')

word = input('Выберите язык: ')

if word == 'kz':
    kz()
elif word == 'ru':
    ru()
elif word == 'kg':
    kg()
else: 
    print('Такого языка в катергори нету')