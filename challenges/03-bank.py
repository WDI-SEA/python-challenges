balance = 1000
finished = False

print("Welcome to Chase bank.")


prompt1 = input('What would you like to do? (deposit, withdraw, check balance)')

if prompt1 == 'deposit':
    deposit = input('How much would you like to deposit?')
    balance = balance + int(deposit)
    print(f'Your current balance is {balance}')

elif prompt1 == 'withdraw':
    withdraw = input('How much would you like to withdraw?')
    balance = balance - int(withdraw)

elif prompt1 == 'check balance':
    print(f'Your current balance is {balance}')

elif prompt1 == 'done' or prompt1 == 'exit':
    finished = True






print("Have a nice day!")

