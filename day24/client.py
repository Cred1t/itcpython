
class Client:
    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.set_password(password)

    def set_password(self, password):
        if len(password) < 8:
            print('Пароль ненадежный ')
        else:
            self.__password = password
    def get_password(self):
        return 'Зашифровано'

    def raw_password(self):
        print('Не разглашайте конфедециальность ваших данных')
        return self.__password
# Интернет магазин BootCamp
# Наш клиент
aman = Client('Амантур', 'aman', 1956)

# Меняем пароль клиента. Принимает только сложные пароли
aman.set_password('12345678')

# Получаем зашифрованнный пароль
# print(aman.get_password())

# Получаем голый пароль. Только разработчики имеют права на разшифровку!!! Приватный доступ 
# print(aman.raw_password())