
class Person:
    def __init__(self, name = 'Не найдено', age = 0):
        self.name = name
        self.__age = age

    def set_age(self, age):
        if age > 100:
            print('Не допустимый возраст')
        else:
            self.__age = age
    
    def get_age(self):
        if self.__age == 0 or self.__age == None:
            return 'Вы не заполнели поле'
        else:
            return self.__age


me = Person( name = 'Amanyr')
print(me.name)
me.set_age(13)
print(me.get_age())