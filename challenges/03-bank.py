print("Welcome to Chase bank.")

def bank_teller(starting_balance):
    option = input("What would you like to do? (deposit, withdraw, view balance): \n")
    balance = starting_balance
    if option == "view balance":
        print(f'Your balance is{balance}')
    elif option == "deposit":
        amount = int(input(f'How much would you like to {option}?\n'))
        balance += amount
        print(f'Your current balance is {balance}')
    elif option == "withdraw":
        amount = int(input(f'How much would you like to {option}?\n'))
        balance -= amount
        print(f'Your current balance is {balance}')
    else:
        print("incorrect input")
        bank_teller(balance)
    
    done = input("Is that all? \n")
    if done == 'yes':
        print("Have a nice day!")
    elif done == "no":
        bank_teller(balance)
    else:
        print("incorrect input")
        bank_teller(balance)

bank_teller(4000)


