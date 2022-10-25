#Create a prompt that asks the user if they would like to display their balance,
#withdraw or deposit. Write three methods to perform these calculations and
#output the result to the user.

#Gather user input using the `input` function. Note that input always returns
#user input as a string. You have to manually convert it to an int or a float
#to make it behave like number. Also, end the input prompt with a \n newline
#character if you want the user to type in on the next line.


print("Welcome to Key bank.")

should_run = True
balance = 0

while should_run:
    print(f'your current balance is {balance}')

    print('What would you like to do?: (Check account balance, withdraw, or deposit)')
    prompt = '> '
    action = input(prompt)
    if action == 'Check account balance':
        print(f'your balance is {balance}')
    elif action == 'withdraw cash':
        print('enter an amount')
        amount = int(input(prompt))
        balance -= amount
    elif action == 'deposit cash':
        print('enter an amount')
        amount = int(input(prompt))
        balance += amount
    else:
        print(f'choice {action} is not valid')

    print('are you finished transacting? (yes/no)')
    done = input(prompt)
    if done == 'yes':
        should_run = False

print("Have a nice day!")
