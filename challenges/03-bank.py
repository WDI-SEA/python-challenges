print("Welcome to Chase bank.")

balance = 4000


def bank_action():
    global balance
    user_choice = input('What would you like to do? (deposit, withdraw, check_balance): ')
    # global user_choice
    if user_choice == 'deposit':
        deposit = int(input('Please enter the amount you\'d like to deposit: '))
        balance += deposit
        print(f'Your balance after depositing is {balance}')
        # continue_banking()
        return balance
    elif user_choice == 'withdraw':
        withdraw = int(input('Please enter the amount you\'d like to withdraw: '))
        balance -=  withdraw
        print(f'Your balance after withdrawing is {balance}')
        # continue_banking()
        return balance
    elif user_choice == 'check_balance':
        print(f'Your current balance is {balance}')
        # continue_banking()
    else:
        print('Please select to deposit, withdraw, or check_balance')
        bank_action()

bank_action()

continue_banking = input('Can we assist you with anything else? (yes/no): ')
if continue_banking == 'no':
    print('Have a great day!')
elif continue_banking == 'yes':
    bank_action()

# def continue_banking(): 
#     input('Can we assist you with anything else? (yes/no): ')
#     if continue_banking == 'no':
#         print('Have a great day!')
#     elif continue_banking == 'yes':
#         bank_action()




# print("Have a nice day!")