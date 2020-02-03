print("Welcome to Chase bank.")

again = 'yes'
balance = 0

while again == 'yes':
    transaction = input('What would you like to do? (deposit, withdraw, check_balance) ')

    if transaction == 'deposit':
        deposit = int(input('How much would you like to deposit? '))
        balance = balance + deposit
    elif transaction == 'withdraw':
        withdrawal = int(input('How much would you like to withdraw? '))
        if balance - withdrawal >= 0:
            balance = balance - withdrawal
        else:
            print('You do not enough money in your account for this transaction.')
    elif transaction == 'check_balance':
        print(f'Your balance is ${balance}')
    else:
        print('There was an error with this transaction, try again.')

    print('Your transaction is complete.')
    again = input('Would you like to make another transaction? (yes/no) ')

