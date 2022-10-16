done = False
balance = 4000
def deposit():
    amount = input("How much would you like to deposit? \n")
    global balance
    balance += int(amount)
    print_balance()
def withdraw():
    amount = input("How much would you like to withdraw? \n")
    global balance
    balance -= int(amount)
    print_balance()
def print_balance():
    print(f"Your current balance is {balance}")

print("Welcome to Chase bank.")
print_balance()
while (not done):
    action = input("What would you like to do? (deposit, withdraw, check_balance \n")
    if (action == "deposit"):
        deposit()
        isDone = input("Are you done? \n")
        if (isDone == "yes"):
            done = True
    elif (action == "withdraw"):
        withdraw()
        isDone = input("Are you done? \n")
        if (isDone == "yes"):
            done = True
    elif (action == "check_balance"):
        print_balance()
        isDone = input("Are you done? \n")
        if (isDone == "yes"):
            done = True

print("Have a nice day!")
