

# ### Challenge 3 - Bank Transactions
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


# ```
# print("Welcome to Chase bank.")

# balance = 4000

# use_whattodo = input("What would you like to do? ")
# # print(use_whattodo)

# use_deposit = int(input("How much would you like to deposit? "))
# print(use_whattodo)

# use_withdraw = int(input("How much would you like to withdraw? "))
# # print(use_withdraw)

# if use_whattodo == "check balance":
#     print(f"Your balance is: {balance} ")
# elif use_howmuchdepo == "deposit":
#      print(f"You deposited: ({use_deposit})")
# elif use_withdraw == "withdraw":
#     print(f"You withdrew: ({use_withdraw})")

# print("Have a nice day!")
transaction = True
balance = 4000

print("Welcome to Chase bank.")

while transaction == True:
    print(f"Your balance is: {balance} ")
    transaction = (input("What would you like to do? deposit or withdraw ?"))

if transaction == "deposit":
    amount = int(input("How much would you like to deposit?:"))
    balance = balance + amount
    print(f" Your balance is now {balance}")
elif transaction == "withdraw":
    amount = int(input("How much would you like to withdraw?:"))
    balance = balance - amount
    print(f" Your balance is now {balance}")
else:
    print("Have a nice day!")



print("Have a nice day!")