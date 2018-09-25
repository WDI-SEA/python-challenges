print("Welcome to Chase bank.")
balance = 4000
while True:
    print('Your current balance is:')
    print(balance)
    print('What would you like to do? (deposit, withdrawl, check_balance)')
    request = input()
    if (request == 'deposit'):
        amt = int(input('How much? '))
        balance += amt
    elif (request == 'withdrawl'):
        amt = int(input('How much? '))
        balance += amt
    elif (request == 'check_balance'):
        print(balance)
    closing = input('Are you done? y/n ')
    if (closing == 'y'):
        break
    elif (closing == 'n'):
        continue
    else:
        print('I\'m going to take that as a no...')
        continue
print("Have a nice day!")
