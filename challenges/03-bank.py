balance = 4000
transaction = True
print("Welcome to Chase bank.")
while transaction == True:
    print(f"Your current balance is: {balance}")
    transaction = (input("What would you like to do? (deposit or withdraw): "))

    if transaction == "deposit":
        amount = int(input("Enter deposit amount: "))
        balance += amount
        print(f"Your new balance is {balance}")
    elif transaction == "withdraw":
        amount = int(input("Enter withdrawal amount: "))
        balance -= amount
        print(f"Your current balance is {balance}")
    else:
        print("Anything else? (y/n)")

print("Have a nice day!")

