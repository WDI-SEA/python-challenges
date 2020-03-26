print("Welcome to Chase bank.")

bal = 4000

def deposit():
    amount = float(input('How much would you like to deposit?\n'))
    return amount

def withdraw():
    amount = float(input('How much would you like to deposit?\n'))
    return amount

def balance():
    global bal
    print(f'Your current balance is\n {bal}')
    ans = input('What would you like to do? (deposit, withdraw, check_balance)\n')
    if (ans == 'deposit'):
        d = deposit()
        bal = int(bal + d)
        print(f'Your current balance is {bal}')
    elif (ans == 'withdraw'):
        w =withdraw()
        bal = int(bal - w)
        print(f'Your current balance is {bal}')
    elif (ans == 'check_balance'):
        print(f'Your current balance is {bal}')
   

balance()
while (True):
    ans = input('Are you done?\n')
    if (ans == 'no'):
        balance()
    elif (ans == 'yes'):
        print('Thank you!')
        break

print("Have a nice day!")

