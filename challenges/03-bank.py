print("Welcome to Chase bank.")
print("Have a nice day!")
balance = 4000
def welcome(name):
    print("Welcome to Chase bank.")
def withdraw():
    pass
def deposit():
    amount = (input("How much would you like to deposit?"))
    global balance
    balance += amount

def check_balance(balance):
    print('Your current balance is', balance)


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
