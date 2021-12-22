

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
print("Welcome to Chase bank.")

balance = 4000

use_whattodo = input("What would you like to do? ")
print(use_whattodo)
if use_whattodo == "check balance":
    print(f"Your balance is: {balance} ")
elif use_howmuchdepo == "deposit":
     use_howmuchdepo == int(input("How much would you like to deposit?"))
     print(f"You deposited: ({use_howmuchdepo})")

# use_howmuchdepo = int(input("How much would you like to deposit?")

# if use_whattodo == 'deposit':
#     print(use_howmuchdepo)
    
   


# use_areyoudone = input("Are you done?")
# print(use_areyoudone)



print("Have a nice day!")
