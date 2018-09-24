print("Welcome to Chase bank.")

current_balance = 0

transaction = ''

while transaction != 'exit':
    transaction = input('What would you like to do today? (deposit, withdraw, check_balance, exit)\n')
    if transaction == 'deposit':
        amount = int(input('How much would you like to deposit?\n'))
        current_balance += amount
    elif transaction == 'withdraw':
        amount = int(input('How much would you like to withdraw?\n'))
        current_balance -= amount
    elif transaction == 'check_balance':
        print('Your current balance is ${}\n'.format(current_balance))
    print('--------------------------------------------')
        
print("Have a nice day!")
