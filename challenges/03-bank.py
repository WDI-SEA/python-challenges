# Create a prompt that asks the user if they would like to display their balance, withdraw or deposit. 
# Write three methods to perform these calculations and output the result to the user.

# Gather user input using the input function. 
# Note that input always returns user input as a string. 
# You have to manually convert it to an int or a float to make it behave like number. 
# Also, end the input prompt with a \n newline character if you want the user to type in on the next line.

balance = 4000
transaction = True

print("Welcome to Chase bank.")
while transaction == True:
    action = (input('withdraw, deposit or view balance? '))

    if action == 'deposit':
        amount = int(input('Enter deposit amount: '))
        balance += amount
        print(f'Your new balance is {balance}')
    elif action == 'withdraw':
        amount = int(input('Enter withdrawal amount: '))
        balance -= amount
        print(f'Your new balance is {balance}')
    elif action == 'view balance':
         print(f'Your current balance is: {balance}')
    else:
        print('Please pick a transaction, withdraw or deposit.')

    continue_action = input('Are you done? (y/n): ')

    if continue_action == 'y':
        transaction= False
        print("Have a nice day!")
        break