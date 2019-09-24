# print("Welcome to Your-bank.")
# print("Have a nice day!")

current_balance = 0
print(f"Your balance is {current_balance}")
is_done = False

while is_done == False:
    response = input('What would you like to do? (deposit, withdraw, check_balance)?')
    if response == 'deposit' or 'Deposit':
        action = int(input('How much would you like to deposit?'))
        current_balance = current_balance + action
        print(f'Your current balance is {current_balance}')
        done_check = input('Are you done? yes/no')

    elif response == 'withdraw':
        current_balance = current_balance - action
        print(f'Your current balance is {current_balance}')
    elif response == 'balance': 
        print(f'Your current balance is {current_balance}')
    else:
        input('Please respond with deposit, withdraw, or check_balance.')
        is_done = input('Are you done?')
    
    if done_check== 'yes':
        print('Have a nice day!')
        is_done = True
    else:
        response

