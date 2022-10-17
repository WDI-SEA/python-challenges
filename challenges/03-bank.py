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

should_run = True
balance = 0

while should_run:
    print("what would you like to do? (deposit, withdraw, check_balance)")
    prompt = '> '
    action = input(prompt)

    if action == 'deposit':
        print('enter an amount')
        amount = int(input(prompt))
        balance += amount
    elif action == 'withdraw':
        print("enter an amount")
        amount = int(input(prompt))
        balance -= amount
    elif action == "check_balance":
        print(f'your current balance is: {balance}')
    else:
        print(f'choice {action} not valid. lets get it together, user.')

    print('are you like done or whatever (yes/no)')
    done = input(prompt)
    if done == 'yes':
        should_run = False


print("Have a nice day!")

