print("Welcome to Chase bank.")

inAccount = True

balance = 0

while inAccount:
    print(f'Your current balance is: {balance}')
    print('What would you like to do? (deposit, withdraw, check_balance)')
    action = input('-> ')
    if (action == 'deposit'):
        print('How much would you like to deposit?')
        deposit = input('-> ')
        balance = int(deposit)
    elif (action == 'withdraw'):
        print('How much would you like to withdraw?')
        withdraw = input('-> ')
        balance = int(withdraw)
    elif (action == 'check_balance'):
        print(f'Your current balance is: {balance}')
    else:
        print(f'Invalid Action, Please try again.')

    print('Would you like to continue?')
    done = input('-> ')
    if done == 'no':
        inAccount = False

print("Have a nice day!")
