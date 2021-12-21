print("Welcome to Chase bank.")
again = 'n'
balance = 4000
def statement(balance): 
        operation = input('Would you like to display, withdraw, or deposit from your balance? (display, withdraw, deposit) \n' )
        if operation == 'display':
            print(f'Your balance is: {balance}')
            again = input('Are you done? (y/n)\n')
        elif operation == 'withdraw':
            amount = input(f'Your balance is: {balance}. How much would you like to withdraw? \n')
            new_balance = balance - int(amount)
            print(f'your new balance is {new_balance}')
            balance = new_balance
            again = input('Are you done? (y/n)\n')
        elif operation == 'deposit':
            amount = input(f'Your balance is: {balance}. How much would you like to deposit? \n')
            new_balance = balance + int(amount)
            print(f'your new balance is {new_balance}')
            balance = new_balance
            again = input('Are you done? (y/n)\n')
        if again == 'n':
            statement(balance)
        

statement(balance)
print("Have a nice day!")

