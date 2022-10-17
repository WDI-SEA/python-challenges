

def bank_transanctions():
    action = input("What would you like to do? (deposit, withdraw, check_balance)\n")
    global balance
    if action == "deposit":
        amount = float(input("How much would you like to deposit?\n"))
        balance += amount
        print(f'Your current balance is ${balance}')
    elif action == "withdraw":
        amount = float(input("How much would you like to withdraw?\n"))
        if balance < amount:
            print(f'You only have ${balance}')
        else:
            balance -= amount
            print(f'Your current balance is ${balance}')
    elif action == "check_balance":
        print(f'Your current balance is ${balance}')
    else:
        print('Wrong action! Please choose deposit, withdraw, or check_balance')
    more_action = input("Are you done?\n")
    if more_action == "no":
        bank_transanctions()
    else:
        print("Thank you!")


balance = 0.00
print("Welcome to Chase bank.")
print("Have a nice day!")
bank_transanctions()
