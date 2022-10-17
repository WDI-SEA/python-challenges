print("Welcome to Chase bank.")
print("Have a nice day!")

def atm():
    global done
    global balance_two

    while(done != 'yes'):
        response = input("What would you like to do at this atm?\n")

        if(response  == 'check_balance'):
            print("Your balance is", balance_two)
        elif (response == 'withdraw'):
            amount = int(input(f"How much would you like to {response}\n"))
            balance_two -= amount
            print("Your balance is now", balance_two)