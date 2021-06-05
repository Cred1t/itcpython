
# Глобальный область видимости
a = 6
def myprint(d):
    # Локальный область видимости
    print(d * a)
# print(x)
myprint(2)