print("Welcome to Chase bank.")
print("Have a nice day!")

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

def bankSim():
    done = 'no'
    current_balance = None
    while (done.lower() == 'no'):
        if current_balance == None:
            current_balance = input('Please enter your current balance\n')
            current_balance = int(current_balance)
        bank_method = input('What would you like to do? (deposit, withdraw, check_balance)\n')
        if bank_method == 'deposit':
            dep_amt = input('How much would you like to deposit?\n')
            dep_amt = int(dep_amt)
            current_balance = current_balance + dep_amt
            print(f'Your new balance is {current_balance}')
        elif bank_method == 'withdraw':
            with_amt = input('How much would you like to withdraw?\n')
            with_amt = int(with_amt)
            if current_balance - with_amt < 0:
                with_amt = input('You do not have enough money to withdraw this amount. Select a different amount to withdraw.\n')
                with_amt = int(with_amt)
                current_balance = current_balance - with_amt
                print(f'Your new balance is {current_balance}')
            else:
                current_balance -= with_amt
                print(f'Your new balance is {current_balance}')    
        elif bank_method == 'check_balance':
            print(f'You have ${current_balance} in your account')
        done = input('Are you done with this funky bank app? (yes/no)')
        

bankSim()