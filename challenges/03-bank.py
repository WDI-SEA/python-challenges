balance = 3000
print("Welcome to Chase bank.")
method = input("What would you like to do? (deposit, withdraw, check_balance)\n")
if method == "check_balance":
    print ("Your balance is", balance)
elif method == "deposit" or method == "withdraw":
    amount = int(input(f"How much would you like to {method}?\n"))
    if method == "deposit":
        balance += amount
    else:
        balance -= amount
    print("Your balance is", balance)
else:
    print("Wrong input. Please try again.")
print("Have a nice day!")

# age = input("How old are you?\n")
# age = int(age)
# Here is a sample output:

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