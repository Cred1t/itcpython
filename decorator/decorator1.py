def decorator_function(func):
    def inner():
        print('Доброе утро')
        func()
        print('ДОбрый верчер')

    return inner


def answer(func):
    def inner():
        func()
        print('Ваалейкум Ассалоом')

    return inner


@answer
def hello():
    print('Ассалоому Алейкум')


hello()