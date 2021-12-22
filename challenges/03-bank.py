
balance = 4000
transaction = True

print("Welcome to Chase bank.")
while transaction == True:
    print(f'Your current balance is: {balance}')
    action = (input('What would you like to do today? (withdraw or deposit): '))

    if action == 'deposit':
        amount = int(input('Enter deposit amount: '))
        balance += amount
        print(f'Your new balance is {balance}')
    elif action == 'withdraw':
        amount = int(input('Enter withdrawal amount: '))
        balance -= amount
        print(f'Your new balance is {balance}')
    else:
        print('Please pick a transaction action!')

    continue_action = input('Are you done? (y/n): ')

    if continue_action == 'y':
        transaction= False
        print("Have a nice day!")
        break
