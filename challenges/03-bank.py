print("Welcome to Chase bank.")
print("Have a nice day!")

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

def bank_prompt() :

    user_prompt = input('Would you like to do? (deposit, withdraw, check_balance) ')
    withdraw = int(input('How much would you like to withdraw? '))
    deposit = int(input('How much are you depositing? '))
    balance = 4000

    if user_prompt == withdraw:
        print(balance - withdraw)
    elif user_prompt == deposit:    
        print(balance + deposit)
    elif user_prompt == 'check_balance':
        print(balance)

bank_prompt()