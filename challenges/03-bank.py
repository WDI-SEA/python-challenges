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


def banking():
    balance = 5000
    print("Welcome to Chase bank.")
    print('Your current balance is: ', balance)
    action = input('What would you like to do? (deposit, withdraw, check_balance)')
    if action == 'deposit':
        amt = int(input(f'How much would you like to {action}?'))
        newBalance = (balance + amt)
        print('Your new balance is: ', newBalance)
    if action == 'withdraw':
        amt = int(input(f'How much would you like to {action}?'))
        newBalance = balance - amt
        print('Your new balance is: ', newBalance)
    if action == 'check_balance':
        print('Your balance is: ', balance)
    done = input('Are you finished with your banking needs today? (yes, no)')
    if done == 'yes':
        print("Have a nice day!")
    elif done == 'no':
        balance = newBalance
        banking()

banking()


