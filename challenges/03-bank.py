print("Welcome to Chase bank.")
balance = 4000
print(f'Your curent balance is\n {balance}')
def bank():
    global balance
    transaction = input('What would you like to do? (deposit, withdraw, check_balance)\n')
    if transaction == 'check_balance':
        print(f'your current balance is {balance}')
    else:
        global amount 
        amount = int(input(f'How much would you like to {transaction}?\n'))
        
    if transaction == 'deposit':
        
        balance = balance + amount
        print(f'your balance is {balance}')
    elif transaction == 'withdraw':
        balance = balance - amount 
        print(f'your balance is {balance}')
    # else: print('nothing')

    done = input("are you done? ('yes' or 'no')\n")

    if done == 'no':
        bank()
    else:
        print("Have a nice day!")

bank()

