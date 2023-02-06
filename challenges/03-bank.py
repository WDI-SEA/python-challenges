print("Welcome to Chase bank.")
print("Have a nice day!")


balance = 4000

def check_balance():
    print("Your current balance is", balance)

def deposit(amount):
    global balance
    balance += amount
    print("Your current balance is", balance)

def withdraw(amount):
    global balance
    if balance >= amount:
        balance -= amount
        print("Your current balance is", balance)
    else:
        print("Insufficient balance")

while True:
    action = input("What would you like to do? (deposit, withdraw, check_balance)\n")
    if action == "check_balance":
        check_balance()
    elif action == "deposit":
        deposit_amount = int(input("How much would you like to deposit?\n"))
        deposit(deposit_amount)
    elif action == "withdraw":
        withdraw_amount = int(input("How much would you like to withdraw?\n"))
        withdraw(withdraw_amount)
    else:
        print("Invalid action")