

operators = {
    'megacom': [
        '0558',
        '0551',
        '0555',
        '0557',
        '0553',
        '0996',
        '0550',
        '0559',
    ],
    'beeline': [
        '0770',
        '0777',
        '0778',
        '0776',
        '0771',
        '0222'
    ],
    'Ошка': [
        '0700',
        '0999',
        '0701',
        '0702'
    ],
    'gorod': [
        '03222',
        '03231',
        '03200',
        '03230',
        '03211',
    ]
}
def check_phone_number(nomer):
    if len(nomer) == 10 and nomer[0] == '0':
        print('Номер телефона правильный')
        code = nomer[0:4]
        print(nomer)
        if code in operators['Ошка']:
            print('Ваш оператор Ошка')
        elif code in operators['megacom']:
            print('Ваш оператор Megacom')
        elif code in operators['beeline']:
            print('Ваш оператор Beeline')
        code = nomer[0:5]
        if code in operators['gorod']:
            print('Городской номер')
    else:
        print('Вы ввели неправильный номер')
phone = input('Введите номер телефона: ')
# phone2 = input('Введите номер телефона 1: ')
check_phone_number(phone)
# check_phone_number(phone2)


def translate():
    print('Say Hello')

def getFullName(fname, lname):
    return fname + ' ' + lname