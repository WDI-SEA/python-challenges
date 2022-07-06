def bankTrip(balance):    
    
    action = input('What would you like to do? (deposit, withdraw, check_balance)\n')

    if(action=='deposit'):
        amount = input('How much would you like to deposit?')
        balance += int(amount)
        print(f"Your current balance is {balance}")

    if (action=='withdraw'):
        amount = input('How much would you like to withdraw?')
        balance -= int(amount)
        print(f"Your current balance is {balance}")

    if (action=='check_balance'):
        print(f"Your current balance is {balance}")
    
    keep_going = input('are you done? y/n\n')
    if (keep_going=='n'):
        bankTrip(balance)
    else:
        print("Have a nice day!")


    



print("Welcome to Chase bank.")

balance = int(input('What is your current balance? \n'))

bankTrip(balance)



