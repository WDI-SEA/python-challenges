print("Welcome to Chase Bank!")
balance = 4000
print('Your current balance is \n', balance)


def bank(balance):
    trans = input(
        'What would you like to do: (deposit, withdraw, check_balance)? \n')
    if trans == 'deposit':
        trans_amount = input('How much would you like to deposit' '? \n')
        balance = int(balance) + int(trans_amount)
        print('Your current balance is \n', balance)
        return balance
    elif trans == 'withdraw':
        trans_amount = input('How much would you like to withdraw ? \n')
        balance = int(balance) - int(trans_amount)
        print('Your current balance is \n', balance)
        return balance
    elif trans == 'check_balance':
        print('Your current balance is \n', balance)
    else:
        print('Invalid Transaction -- Please Try Again')
        bank(balance)


bank(balance)

done = input('Are you done: (yes/no)? \n')


def done_check(done):
    if done == 'no':
        bank(balance)
        done = input('Are you done: (yes/no)? \n')
        done_check(done)
    else:
        print("Have a nice day!")


done_check(done)
