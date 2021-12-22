print("Welcome to Chase bank.")

# initialize user balance
user = {
    "balance": 5000,
}

# set conditional for running program
complete = False

# write a method for each kind of transaction
def withdraw():
    wit = int(input("How much would you like to withdraw?\n"))
    user["balance"] -= wit
    print("Your current balance is\n", user["balance"] )

def deposit():
    dep = int(input("How much would you like to deposit?\n"))
    user["balance"] += dep
    print("Your current balance is\n", user["balance"] )

def inquiry():
    print("Your current balance is\n", user["balance"] )

# run transaction functions based off of a string value
def transaction(action):
    if action == "deposit":
        deposit()
    if action == "withdraw":
        withdraw()
    if action == "check_balance":
        inquiry()

while complete == False:
    # ask the user which transaction to perform
    request = input("What would you like to do? (deposit, withdraw, check_balance)\n")
    # run transaction based off of user input
    transaction(request)
    # ask user if they are finished
    done = input("Are you done? (Y/N)\n")
    # update conditional based off of user input
    if done == "Y":
        complete = True
    elif done == "N":
        complete = False

print("Have a nice day!")