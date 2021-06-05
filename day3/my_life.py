year = int(input('Введите год:', ))
my = int(input('Ваш год рождения:', ))
summa = year - my 
month = summa * 12
day = month * 365
hour = day * 24
minute = hour * 60
second = minute * 60

print('Мен', year, 'жыл жашадым' )
print('Мен', month, 'ай жашадым' )
print('Мен', day, 'кун жашадым' )
print('Мен', hour, 'саат жашадым' )
print('Мен', minute, 'минута жашадым' )
print('Мен', second, 'секонд жашадым' )
