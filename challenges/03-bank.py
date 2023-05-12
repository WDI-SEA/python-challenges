balance = 4000

def banking():
    print("Welcome to Chase bank.")

    global balance

    transaction = input("What would you like to do? (deposit, withdraw, balance)\n")

    if transaction == 'deposit':
        deposit_amount = float(input("How much would you like to deposit?\n"))
        balance += deposit_amount
        return f"Your new balance is {balance}."
    elif transaction == 'withdraw':
        withdraw_amount = float(input("How much would you like to withdraw?\n"))
        balance -= withdraw_amount
        return f"Your new balance is {balance}."
    elif transaction == 'balance':
        return f"Your current balance is {balance}."

    print("Have a nice day!")

# print(banking())

def deposit(amount):
    global balance
    balance += amount
    return balance

def withdraw(amount):
    global balance
    if amount <= balance: #check if sufficient balance exists
        balance -= amount
    else:
        print("Insufficient balance.")
    return balance

def check_balance():
    global balance
    return balance

while True:
    print(f"Your current balance is {balance}.")
    transaction = input("What would you like to do? (deposit, withdraw, check_balance)\n")

    if transaction == "deposit":
        amount = int(input("How much would you like to deposit?\n"))
        balance = deposit(amount)
        print(f"Your current balance is {balance}")
    elif transaction == "withdraw":
        amount = int(input("How much would you like to withdraw?\n"))
        balance = withdraw(amount)
        print(f"Your current balance is {balance}")
    elif transaction == "check_balance":
        print(f"Your current balance is {balance}")
    else:
        print("Not a valid input. Select deposit, withdraw, check_balance.\n")

    done = input("Are you done? (yes, no)\n")
    if done.lower() == "yes":
        print("Thank you!")
        break