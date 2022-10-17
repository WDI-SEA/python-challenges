

from operator import truediv


print("Welcome to Chase bank.")

should_run = True
balance = 0

while should_run:
    print(f"your balance: {balance}")

    print('Would you like to deposit, withdraw, check balance, or quit?')
    prompt = "> "
    action = input(prompt)
    if action == 'deposit':
        print("enter an amount")
        amount = int(input(prompt))
        balance += amount
    elif action == 'withdraw':
        print("enter an amount")
        amount = int(input(prompt))
        balance -= amount
    elif action == 'check balance':
        print(f"your current balance is: {balance}")
    elif action == 'quit':
        should_run = False
    else:
        print(f'choice {action} is invalid')
print("Have a nice day!")


