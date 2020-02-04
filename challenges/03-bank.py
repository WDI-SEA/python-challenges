balance = 10
done = False

# Helper functions
def deposit(amount):
    global balance
    balance += amount
    balance = round(balance, 2)
    print(f'Your new balance is ${balance}!\n')

def withdraw(amount):
    global balance
    amount = round(amount, 2)
    if balance >= amount:
        balance -= amount
        print(f'Dispersing {amount}')
        print(f'New balance is {balance}!')
    else:
        print('Sorry, but you are broke.\n')

def check_balance():
    print(f'Your balance is ${balance}!')

# User interaction
print("Welcome to Chase bank.\n")

while not done:
    action = input('What would you like to do? (deposit, withdraw, check_balance) ')

    if action == 'done' or action == 'exit':
        done = True
    elif action == 'balance' or action == 'check_balance':
        check_balance()
    elif action == 'deposit':
        amount = float(input('What amount? '))
        deposit(amount)
    elif action == 'withdraw':
        amount = float(input('What amount? '))
        withdraw(amount)
    else:
        print('Wow, what did you say? ')

print("Have a nice day!")

