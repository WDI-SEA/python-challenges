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

currentBalance = int(input('Your current balance is\n'))
choice = input('What would you like to do? (deposit, withdraw, check_balance)\n')
if choice == 'deposit' or choice == 'withdraw':
    amount = int(input(f'How much would you like to {choice}?\n'))
    if choice == 'deposit':
        currentBalance += amount
        print(f'Your current balance is ${currentBalance}')
    elif choice == 'withdraw' and amount <= currentBalance:
        currentBalance -= amount
        print(f'Your current balance is ${currentBalance}')
    else:
        print('Please enter a valid amount')
elif choice == 'check_balance':
    print(f'Your current balance is ${currentBalance}')
else:
    print('Please enter a valid command')
final = input('Are you done? (y/n)\n')
if final == 'y':
    print('Thank you!')
elif final == 'n':
    choice = input('What would you like to do? (deposit, withdraw, check_balance)\n')
else:
    print('Please enter a valid command')