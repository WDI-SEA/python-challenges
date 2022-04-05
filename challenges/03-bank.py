print("Welcome to Chase bank.")

total = 0.00
done = False

function = input('What would you like to do? (deposit/d, withdraw/w, check_balance/c)\n')

while not done:
    if function == 'deposit' or function == 'd':
        deposit = input('How much would you like to deposit?\n')
        deposited_amount = float(deposit)
        total += deposited_amount
        print('Your current balance is ' + str(total))
        done = input('Are you done? (yes/y, no/n)\n')
        if done == 'yes' or done == 'y':
            done = True
            print("Have a nice day!")
        elif done == 'no' or done == 'n':
            done = False
            function = input('What would you like to do? (deposit, withdraw, check_balance)\n')
    elif function == 'withdraw' or function == 'w':
        withdraw = input('How much would you like to withdraw?\n')
        withdrawn_amount = float(withdraw)
        total -= withdrawn_amount
        print('Your current balance is ' + str(total))
        done = input('Are you done? (yes/y, no/n)\n')
        if done == 'yes' or done == 'y':
            done = True
            print("Have a nice day!")
        elif done == 'no' or done == 'n':
            done = False
            function = input('What would you like to do? (deposit, withdraw, check_balance)\n')
    elif function == 'check_balance' or function == 'c':
        print('Your current balance is ' + str(total))
        done = input('Are you done? (yes/y, no/n)\n')
        if done == 'yes' or done == 'y':
            done = True
            print("Have a nice day!")
        elif done == 'no' or done == 'n':
            done = False
            function = input('What would you like to do? (deposit, withdraw, check_balance)\n')

