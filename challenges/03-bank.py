print("Welcome to Chase bank.")
print("Have a nice day!")

balance = 0
print(f"Your balance is {balance}")

isDone = False

while not isDone:
    method = input("What would you like to do? (deposit, withdraw, check_balance):\n")
    if method == "deposit":
        deposit_amount = int(input("How much would you like to deposit?\n"))
        balance += deposit_amount
    elif method == "withdraw":
        withdraw_amount = int(input("How much would you like to withdraw?\n"))
        balance -= withdraw_amount
    elif method == "check_balance":
        pass
    else:
        print("Sorry, I don\'t understand the input")
    print(f"Your balance is {balance}")
    done = input("Are you done? (yes/no)")
    if done == "yes":
        isDone = True

