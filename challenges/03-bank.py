print("Welcome to Chase bank.")


balance = 4000

def check_balance():
    print("Your current balance is")
    print(balance)

def deposit():
    amount = float(input("How much would you like to deposit?\n"))
    global balance
    balance += amount

def withdraw():
    amount = float(input("How much would you like to withdraw?\n"))
    global balance
    if amount <= balance:
        balance -= amount
    else:
        print("You are broke")

print ("Your current balance is")
print(balance)

while True:
    action = input("What would you like to do? (deposit, withdraw, check_balance)\n")

    if action == "deposit":
        deposit()
        check_balance()
    elif action == "withdraw":
        withdraw()
        check_balance()
    elif action == "check_balance":
        check_balance()
    else:
        print("Invalid action.")

    done = input("Are you done?\n")
    if done == "yes":
        print("Thank you!")
        print("Have a nice day!")


        