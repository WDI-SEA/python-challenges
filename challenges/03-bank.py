# print("Welcome to Chase bank.")
# print("Have a nice day!")


balance = 1000
# define functions first
def display_balance():
    print("Your current balance is", balance)

def withdraw(amount):
    # use global keyword to modify the global variable
    global balance
    # check if the amount is greater than the balance
    balance -= amount
    print("You have withdrawn", amount)
    print("Your new balance is", balance)

def deposit(amount):
    global balance
    # use += to add the amount to the balance
    balance += amount
    print("You have deposited", amount)
    print("Your new balance is", balance)

while True:
    user_input = input("Would you like to display your balance, withdraw or deposit?\n")
    if user_input == "display balance":
        display_balance()
    elif user_input == "withdraw":
        amount = int(input("How much would you like to withdraw?\n"))
        withdraw(amount)
    elif user_input == "deposit":
        amount = int(input("How much would you like to deposit?\n"))
        deposit(amount)
    else:
        print("Invalid input. Please try again.")

