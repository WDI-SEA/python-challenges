print("Welcome to Chase bank.")

should_run = True
balance = 0

while should_run:
    print(f"your current balance is: {balance}")

    print("what would you like to do? (deposit, withdraw, check_balance)")
    prompt = '> '
    action = input(prompt)

    if action =='deposit':
        print('enter an amount')
        amount = int(input(prompt))
        balance += amount
    elif action == 'withdraw':
        print('enter an amount')
        amount = int(input(prompt))
        balance -= amount
    elif action == 'check_balance':
        print(f'your current balance is: {balance}')
    else:
        print(f'choice {action} not valid, lets get it together , user.')

    print('are you done? (yes or no)')   
    done = input(prompt)
    if done == 'yes':
        should_run = False

        
print("Have a nice day!")
