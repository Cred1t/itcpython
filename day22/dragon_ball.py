
magics = {}
enemy = {
    'dragon': 30
}

magic_file = open('magic.txt', 'r')
magic_array = magic_file.readlines()
# text = magic_file.readline()

for cur_magic in magic_array:
    magic_striped = cur_magic.strip()
    magic_splitted = magic_striped.split(',')
    magics[magic_splitted[0]] = float(magic_splitted[1])

print('Ваш противник', enemy)

while enemy['dragon'] != 0:
    udar = input('Выберите удар: ')
    u = magics[udar]
    enemy['dragon'] = enemy['dragon'] - u
    print('XP врага: ', enemy['dragon'])

print('Вы победили. У врага: ', enemy['dragon'])

# print(magic_file.read())