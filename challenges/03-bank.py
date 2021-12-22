### Challenge 3 - Bank Transactions
# Create a prompt that asks the user if they would like to display their balance,
# withdraw or deposit. Write three methods to perform these calculations and
# output the result to the user.
# Gather user input using the `input` function. Note that input always returns
# user input as a string. You have to manually convert it to an int or a float
# to make it behave like number. Also, end the input prompt with a \n newline
# character if you want the user to type in on the next line.

# ```
# age = input("How old are you?\n")
# age = int(age)
# ```

# Here is a sample output:

# ```
# Your current balance is
# 4000
# What would you like to do? (deposit, withdraw, check_balance)
# deposit
# How much would you like to deposit?
# 1000
# Your current balance is 5000
# Are you done?
# yes
# Thank you!

def bank():
    balance = 4000
    print("Welcome to Chase bank.")
    print(f"Your current balance is {balance}")
    display = input("What would you like to do? check_balance, withdraw, or deposit\n")
    if display == "check_balance":
        print(f"Your current balance is {balance}")
        done = input("Are you done?: ")
        if done == "yes" or done == "y":
            print("Thank you!")
            return
        elif done == "no" or done == "n":
            bank()
    elif display == "withdraw":
        withdraw = int(input("How much would you like to withdraw?: "))
        balance = balance - withdraw
        print(f"Your new balance is {balance}")
        done = input("Are you done?: ")
        if done == "yes" or done == "y":
            print("Thank you!")
            return
        elif done == "no" or done == "n":
            bank()
    elif display == "deposit":
        deposit = int(input("How much would you like to deposit?: "))
        balance = balance + deposit
        print(f"Your new balance is {balance}")
        done = input("Are you done?: ")
        if done == "yes" or done == "y":
            print("Thank you!")
            return
        elif done == "no" or done == "n":
            bank()
    else:
        bank()

bank()

