
import random

class Bank:
    def __init__(self, bank_name, bank_balance):
        self.bank_name = bank_name
        self.bank_balance = bank_balance
    # Информация о банке
    def bank_info(self):
        print('Добро пожаловать: ', self.bank_name)

    # Оборот банка
    def get_bank_balance(self):
        print('Общий баланс банка: ', self.bank_balance)

    # Открытие счета
    def create_account(self, client_name, password):
        rnd = random.randint(1000,2000)
        self.account = {
            rnd: {
                'name': client_name,
                'password': password,
                'balance': 0 
            }
        }
        print(
            'Ваш аккаунт открыт:','\n',
            'Имя: ',self.account[rnd]['name'],'\n',
            'Пароль: ',self.account[rnd]['password'],'\n',
            'Баланс: ',self.account[rnd]['balance'],'\n',
        )
        print('Счет вашего аккаунта: ', rnd)
        return rnd

    # Данные о счете clienta
    def get_account(self, nomer):
        print('Ваш счет: ', self.account[nomer])
    
    # Получаем баланс на счете
    def get_balance(self, nomer):
        print(
            'Деньги на вашем счете: ', 
            self.account[nomer]['balance']
        )
    def add_money_to_balance(self, nomer, money):
        self.account[nomer]['balance'] = self.account[nomer]['balance'] + money
        print('Ваши счет увеличелись на: ', money)

    # Создаем электронную карту
    def create_card(self, client_name, type, password):
        pass

    def get_credit_card(self, client_name):
        pass


