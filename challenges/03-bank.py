balance = 50
done = 'no'

def bank():
    print("Welcome to Chase bank.")
    global balance
    global done
    while done != 'yes':
        to_do = input('What would you like to do? (deposit, withdraw, check_balance) \n')
        if to_do == 'deposit':
            amount = int(input('How much would you like to depoist?\n'))
            balance += amount
            print(f'Your current balance is {balance}')
            done = input('Are you done? (yes or no) \n')
        elif to_do == 'withdraw':
            amount = int(input('How much would you like to withdraw?\n'))
            balance -= amount
            print(f'Your current balance is {balance}')
            done = input('Are you done? (yes or no)\n')
        elif to_do == 'check_balance':
            print(f'Your current balance is {balance}')
            done = input('Are you done? (yes or no) \n')
    print("Have a nice day!")
bank()




