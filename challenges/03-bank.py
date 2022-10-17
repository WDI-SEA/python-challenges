print("Welcome to Chase bank.")
should_run = True
balance = 0
while should_run:
    print(f'your current balance is {balance}')

    print('What would you like to do today: display balance, withdraw, or deposit')
    prompt = '> '
    action = input(prompt)
    if action == 'display balance':
        print(f'your balance is {balance}')
    elif action == 'withdraw':
        print('enter an amount')
        amount = int(input(prompt))
        balance -= amount
    elif action == 'deposit':
        print('enter an amount')
        amount = int(input(prompt))
        balance += amount
    else:
        print(f'choice {action} is not valid. please input an accurate action')

    print('are you finished? (yes/no)')
    done = input(prompt)
    if done == 'yes':
        should_run = False

print("Have a nice day!")

