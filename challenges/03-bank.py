print("Welcome to Chase bank.")

balance = 4000
transaction = True

while transaction == True:
    print(f"Your current balance is {balance}")
    response = (input("What would you like to do? (deposit, withdraw, check _balance) "))

    if response == "deposit":
        amount = int(input("How much would you like to deposit?"))
        balance += amount
        print(f"Your current balance is {balance}")
    elif response == "withdraw":
        amount = int(input("How much would you like to withdraw? "))
        balance -= amount
        print(f"Your current balance is {balance}")
    else:
        print("Are you done? (y/n)")


print("Have a nice day!")

