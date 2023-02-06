print("Welcome to Chase bank.")

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
# balance = 3

def bank():
    print('Your current balance is \n' + str(balance) + '\nWhat would you like to do? (deposit, withdraw, check_balance)')
    choice = input()
    if choice == 'deposit':
        print('How much would you like to deposit?')
        # this doesnt globally change them rn
        # global balance
        balance += int(input())
        print('Your current balance is ' + str(balance) + '\nAre you done?')
        if input() == 'yes':
            print('Thank you!')
        else: 
            bank()
    elif choice == 'withdraw':
        print('How much would you like to withdraw')
        # global balance
        balance -= int(input())
        print('Your current balance is' + str(balance) + '\nAre you done?')
        if input() == 'yes':
            print('Thank you!')
        else: 
            bank()
    elif choice == 'check_balance':
        print('Your current balance: ' + str(balance) + '\nAre you done?')
        if input() == 'yes':
            print('Thank you!')
        else: 
            bank()
    else:
        print('incorrect')

# bank()

# so we had to have it run like this not as a function

is_running = True

balance = 0

while is_running:
    # do banking activities
    prompt = '↳ '
    #ask the user what they wana do 
    print('whatchawanna do (depo, with, check)')
    transaction = input(prompt)

    if transaction == 'depo':
        print('how much ?')
        # global balance
        balance += int(input(prompt))
        print(f'ur balance {balance}')
    elif transaction == 'with':
        print('how much ?')
        # global balance
        balance -= int(input(prompt))
        print(f'ur balance {balance}')
    elif transaction == 'check':
        print(balance)
    else:
        print('huh ?')
    print('are you done ? [y/n]')
    is_done = input(prompt)
    if is_done == 'y':
        print("Have a nice day!")
        is_running = False

