
import bank

demir = bank.Bank(
    bank_name = 'Demir Bank',
    bank_balance = 750_000_000.00
)

demir.bank_info()
demir.get_bank_balance()
nomer = demir.create_account(
    client_name='Amantyr',
    password= 1234
)

print('Я получил номер счета', nomer)

# Пополнение счета в банке
demir.add_money_to_balance(nomer, 7800)

# Еще раз проверяю свой счет
demir.get_account(nomer)
