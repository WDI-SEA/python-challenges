print("Welcome to Chase bank.")
print("Have a nice day!")

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