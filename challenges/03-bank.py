print("Welcome to Chase bank.")

transaction = input(
    'What would you like to do? (deposit, withdraw, display)')
balance = 4000

if transaction == 'display':
    print(f'current balance of {balance}')

elif transaction == 'deposit':
    amount_deposit = input('how much would you like to deposit')
    print(f'you have a total amount of {int(balance) + int(amount_deposit)}')
    print('Have a gooood day')
elif transaction == 'withdraw':
    amount_withdraw = input('how much would you like to withdraw')
    print(f'you have a total amount of {int(balance) - int(amount_withdraw)}')
    print('Have a gooood day')

else:
    print('invalid transaction! Try again!')
