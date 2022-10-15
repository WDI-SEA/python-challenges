print("Welcome to Chase bank.")
balance = 0
print("Your current balance is:")
print(balance)

def more_transactions():
    again = input("Would you like to make another transaction? y/n ")
    if again == "y":
        atm()
    elif again == "n":
        print("Have a nice day!")
    else:
        print("Please input a valid response.")
        more_transactions()

def atm():
    global balance
    transaction = input("What would you like to do? (deposit, withdraw, check balance) ")
    if transaction == "deposit":
        deposit = input("How much would you like to deposit? ")
        balance += int(deposit)
        print("Your balance is now:")
        print(balance)
        more_transactions()
    elif transaction == "withdraw":
        withdraw = input ("How much would you like to withdraw? ")
        balance -= int(withdraw)
        print("Your balance is now:")
        print(balance)
        more_transactions()
    elif transaction == "check balance":
        print("Your current balance is:")
        print(balance)
        more_transactions()
    else:
        print("Invalid transaction type. Please try again")
        atm()

atm()