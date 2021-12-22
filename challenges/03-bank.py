user_done =  True
user_balance = 4000
user_value = 0


def bank_operation(string, user_balance):
    
    if string == 'deposite':
        user_value = int(input('How much would you like to deposite?\n'))
        return user_value + user_balance
    elif string == 'withdraw':
        user_value = int(input('How much would you like to withdraw?\n'))
        return user_balance - user_value
    elif string == 'check_balance':
        return user_balance
    else:
        print('That comand is not known please choose one of the following (deposit, withdraw, check_balance)')
        return user_balance


def exit_function(string):
    if string == 'No':
       return False
    else:
        return True



print("Welcome to Chase bank.")

while user_done:
    print(f'Your balance is {user_balance}')
    user_input = input('What would you like to do? (deposite, withdraw, check_balance)\n')
    user_balance = bank_operation(user_input, user_balance)
    print(f'Your balance is {user_balance}')
    user_exit = input('Can we help you any more?\n')
    user_done = exit_function(user_exit)

print("Have a nice day!")






