
class Person:
    def __init__(self, name, age, idcard, pos):
        self.name = name
        self.idcard = idcard
        self.age = age
        self.pos = pos

    def to_work(self):
        print('sleep')

class Student(Person):
    status = 'student'
    def to_work(self):
        print('study')


class Teacher(Person):
    status = 'teacher'
    def to_work(self):
        print('teach')

class Programmer(Person):
    pass



jimm = Teacher(
    name = 'Jimmi',
    age = 46,
    idcard = 121212,
    pos = 'Ментор'
)

me = Student( 
    name = 'Mike',
    age = 33,
    idcard = 121219,
    pos = 'Student'
)

zalkarbek = Programmer(
    name = 'zalkarbek',
    age = 18,
    idcard = 1212122,
    pos = 'Programmer'
)


me.to_work()
jimm.to_work()
zalkarbek.to_work()