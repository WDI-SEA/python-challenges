from multiprocessing.dummy import current_process


print("Welcome to Chase bank.")

user_done = False
current_balance = 4000

def deposit(balance,amount):
    new_balance = int(balance) + int(amount)
    return new_balance


def withdraw(balance,amount):
    new_balance = int(balance) - int(amount)
    return new_balance

while not user_done:
    print('Your current balance is \n {}'.format(current_balance))

    transaction_type = input('What would you like to do?(deposit, withdraw, check_balance)  \n>')

    transaction_list = ('deposit', 'withdraw', 'check_balance')

    while not transaction_type in transaction_list:
        transaction_type = input('You made an invalid selection. Please type one of the following\n deposit, withdraw, check_balance\n >')

    if transaction_type == 'deposit':
        amount = input('How much would you like to deposit? \n>')
        current_balance = deposit(current_balance, amount)
    elif transaction_type == 'withdraw':        
        amount = input('How much would you like to withdraw? \n>')
        while int(current_balance) < int(amount):
            print('Sorry you cannot withdraw more than what you have in your account. (Maximum withdrawable amount : {}). \n>'.format(current_balance))
            amount = input('Enter another amount : \n>')
        current_balance = withdraw(current_balance, amount)    

    print('Your current balance is {}'.format(current_balance))

    user_response = input('Are you done? (yes/no)\n>')

    if  user_response == 'yes':
        user_done = True
        print('Have a nice day!')
        break