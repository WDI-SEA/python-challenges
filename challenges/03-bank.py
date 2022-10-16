print("Welcome to Chase bank.")

def bank():
    balance = 4000
    options = 'bwd'
    bank_opt = input(f'''
    Good Morning!
    {balance}
    What would you like to do?
    - See balance: [b]
    - Withdraw: [w]
    - Deposit: [d]
    ''')
    
    if bank_opt in options:
        if bank_opt == 'b':
            print(f'current balance is: {balance}')
        elif bank_opt == 'w':
            amount = int(input('How much would you like to withdraw? '))

            if amount > balance:
                print('Sorry, insufficient funds.')
            elif amount <= balance:
                print(f'Withdrawing {amount}, remaining balance is {balance - amount}.')
            else: 
                print('Error, try again!')

        elif bank_opt == 'd':
            deposit = int(input('''
            How much would you like to deposit? 
            '''))
            
            if deposit > 0:
                print(f'Depositing {deposit}, current balance {balance + deposit}.')
            elif deposit < 1:
                print('Nothing to deposit. Try again.')
            else: 
                print('Error')

        else:
            print('Invalid selection. Please try again.')
    
    else: 
        print('Error, incorrect input. Try again.')
bank()



print("Have a nice day!")

