print("Welcome to Chase bank.")


def bank():
    current_balance = 0 
    print("What would you like to do? (deposit, withdraw, check_balance)")
    action = input('>')
    if action == 'deposit':
        print("How much would you like to deposit?")
        amt = input('>')
        current_balance += int(amt)
        print(f'Your current balance is {current_balance}')
    elif action == 'withdraw':
        print("How much would you like to withdraw")
        amt = input('>')
        if int(amt) > current_balance:
            print("Insufficient Funds")
        else:
            current_balance -= int(amt)
            print(f'Your current balance is {current_balance}')
    elif action == 'check_balance':
        print(f'Your current balance is {current_balance}')
    else:
        print('Action not recognized. Please try again')
    print("Are you done? (yes/no)")
    repeat = input('>')
    if repeat == "no":
        bank()

bank()

print("Have a nice day!")

