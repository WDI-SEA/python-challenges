print("Welcome to Chase bank.")
print("Have a nice day!")

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
balance = 420
opener = input("balance, withdraw, deposit?")
if opener == 'balance':
    print(balance)
elif opener == 'withdraw':
    print(balance)
    withdraw = input('how much to withdraw')
    withdraw = int(withdraw)
    balance -= withdraw
    print(balance)
elif opener == 'deposit':
    print(balance)
    deposit = input('how much to deposit')
    deposit = int(deposit)
    balance += deposit
    print(balance)
else:
    print('no comprendo')


