print("Welcome to Chase bank.")

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

balance = 4000

prompt = '>'
print(f'Your current balance is \n{balance}')
print(f'What would you like to do? (deposit, withdraw, check_balance)')

operator = input(prompt)

if operator == 'deposit' or operator == 'withdraw':
    print(f'How much would you like to {operator}?')
    num = input(prompt)
    if operator == 'deposit':
        balance += float(num)
    elif operator == 'withdraw':
        balance -= float(num)
print(f'Your current balance is: ${balance}\n')
print('Are you done?')

response = input(prompt)
if response == 'yes':
    print("Have a nice day!")
elif response == 'no':
    print("Well that's all that I have the energy for right now")

