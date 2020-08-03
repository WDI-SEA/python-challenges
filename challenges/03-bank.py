# print("Welcome to Chase bank.")
# print("Have a nice day!")

current_balance = 4000

def action_input():
    return input('What would you like to do? (deposit, withdraw, check_balance?:\n')

def atm(balance):
    print(f'Your current balance is\n{balance}')
    action = action_input()
    if action == 'deposit':
        amount = input('How much would you like to deposit?:\n')
        new_balance = int(balance) + int(amount)
        print(f'Your current balance is {new_balance}')
    elif action == 'withdraw':
        amount = input('How much would you like to withdraw?:\n')
        new_balance = int(balance) - int(amount)
        print(f'Your current balance is {new_balance}')
    elif action == 'check_balance':
        print(f'Your current balance is {balance}')
    finished = input('Are you done?:\n')
    if finished == 'yes':
        print("Have a nice day!")
    elif finished == 'no':
        atm(new_balance)
        
atm(current_balance)