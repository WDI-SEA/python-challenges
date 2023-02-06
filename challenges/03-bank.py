print("Welcome to Chase bank.")
print("Have a nice day!")

currentBalance = 0
again = ''

def deposit():
    value = input('How much would you like to deposit: ')
    global currentBalance
    currentBalance = currentBalance + int(value)
    print('Your current balance is ', currentBalance)

def withdraw():
    value = input('How much would you like to withdraw: ')
    global currentBalance
    currentBalance = currentBalance - int(value)
    print('Your current balance is ', currentBalance)

def check_balance():
    global currentBalance
    print('Your current balance is ', currentBalance)


def run():
    action = input('What would you like to do? (deposit, withdraw, check_balance): ')
    if(action == 'deposit'):
        deposit()
    elif(action == 'withdraw'):
        withdraw()
    else:
        check_balance
    global again    
    again = input('Are you done(yes/no): ')



run()
if(again == 'no'):
    run()
else:
    again = 'yes'
    print('thank you')
    

