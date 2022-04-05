print("Welcome to Chase bank.")

balance = 5000
choice = 'no'

print(f'Your current balance is: \n {balance}')

while balance != 0 or choice == 'no':

    operation = input('What would you like to do? (deposit, withdraw, check_balance) \n')

    if operation == 'deposit':
        deposit = input('How much would you like to deposit? \n')
        deposit = int(deposit)
        balance = balance + deposit
        print(f'Your current balance is : {balance}')
    elif operation == 'withdraw':
        withdraw = input('How much would you like to withdraw? \n')
        withdraw = int(withdraw)
        if withdraw > balance:
            print('You are withdrawing an amount greater than your balance.')
        else:
            balance = balance - withdraw
            print(f'Your current balance is : {balance}')
    elif operation == 'check_balance':
        print(f'Your current balance is: {balance}')
    
    choice = input('Are you done? \n')
    if choice == 'yes':
        break


# if choice == 'yes':
#     print("Have a nice day!")
print("Have a nice day!")

