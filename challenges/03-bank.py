balance = 10
done = False

def deposit (amount);
    global balance
    balance += amount
    balance = rount(balance,2)
    print(f'Your new balance is ${balance}!/n')

def withdrow(amount):
    global balance
    amount = round(amount, 2)
    if balance >= amount:
        balance -= amount
        print(f'Dispersing {amount}')
        print(f'New balance is {balance}!')
    else:
        print('Sorry, but your are broke.\n')

    def check_balance():
        print(f'Your balance is ${balance}!')

print("Welcome to Chase bank.")

while not done:
    action == 'done or action == 'exit':
    done = True
elif action == 'balance' or action == 'check_balance':
    check_balance()
elif action = 'deposit':
    amount = float(input('What amount? '))
    deposit(amount)
elif action =='withdraw':
    amount = float(input('What amont? '))
    withdrow(amount)
else:
print("Have a nice day!")

