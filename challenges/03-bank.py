# Create a prompt that asks the user if they would like to display their balance, withdraw or deposit. Write three methods to perform these calculations and output the result to the user.

# Gather user input using the input function. Note that input always returns user input as a string. You have to manually convert it to an int or a float to make it behave like number. Also, end the input prompt with a \n newline character if you want the user to type in on the next line.

# age = input("How old are you?\n")
# age = int(age)

# Sample Output:
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

print("Welcome to Chase Bank.")

def bank(): 
    balance = 4000
    print(f'Your current balance is {balance}')
    user_input = input('Would you like to check your balance, withdraw or deposit?')

    if user_input == 'check balance':
        print(f'Your current balance is {balance}') 
    elif user_input == 'withdraw':
        withdraw = int(input('How much would you like to withdraw?'))
        print(f'Your balance after withdrawal is {balance-withdraw} ')
        balance = (balance - withdraw)
    elif user_input == 'deposit':
        deposit = int(input('How much would you like to deposit?'))
        print(f'Your balance after deposit has cleared is {balance + deposit}')
        balance = (balance + deposit)
    else:
        print('Invalid input')

    finished = input('Are you finished?')

    if finished == 'yes':
        print('Thank you for using Chase Bank. Have a nice day!')
    else:
        bank()

bank()

