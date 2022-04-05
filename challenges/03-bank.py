print("Welcome to Chase bank.")
balance = 4000

def transaction():
    global balance
    print(f'Your current balance is {balance}')
    action = input('What would you like to do? (deposit, withdraw, check_balance)\n')
    if action == 'check_balance':
        print(f'Your current balance is {balance}')
    elif action == 'deposit':
        deposit = int(input('How much would you like to deposit?\n'))
        print(f'Your current balance is {balance+deposit}')
        balance = balance+deposit
    elif action == 'withdraw':
        withdraw = int(input('How much would you like to withdraw?\n'))
        print(f'Your current balance is {balance-withdraw}')
        balance = balance-withdraw
    else:
        print('invalid action')
    done = input('Are you done?\n')

    if done == 'yes':
        print("Have a nice day!")
    else:
        transaction()
transaction()

