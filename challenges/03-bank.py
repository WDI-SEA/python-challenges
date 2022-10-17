balance = 8000
def transaction ():
    global balance
    method = input("Would you like to deposit, withdraw, or check_balance)?")
    if method == "check_balance":
        print ("Your balance is", balance)
    elif method == "deposit" or method == "withdraw":
        amount = int(input(f"How much would you like to {method}?\n"))
        if method == "deposit":
            balance += amount
        else:
            balance -= amount
        print("Your balance is", balance)
    else:
        print("Wrong input. Please try again.")
        transaction()


print("Welcome to Chase bank.")
transaction()
print("Have a nice day!")
