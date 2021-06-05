
# for i in range(11):
#     for k in range(11):
#         print(i, '*', k, '=', i * k, end='        ')



roles = ['Admin', 'Maneger', 'Author', 'User', 'Guest']

users = ['Tom', 'Jake', 'Rock', 'John', 'Janet', 'Frank']

# for user in users:
#     print(user, 'is', roles[0])
#     print(user, 'is', roles[1])
#     print(user, 'is', roles[2])
#     print(user, 'is', roles[3])
#     print(user, 'is', roles[4])
#     print()

for user in users:
    for role in roles:
        print(user, 'is', role)
    print()
