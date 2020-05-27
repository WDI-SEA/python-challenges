print("Welcome to Chase bank.")
print("Have a nice day!")

currbal = 4000
deposit = 'deposit'
withdraw = 'withdraw'
check_balance = 'check_balance'
yes = 'yes'

print('Your current balance is')
print(currbal)
action = input('What would you like to do? deposit, withdraw, check_balance?')
if action == deposit:
    depvalue = int(input('How much would you like to deposit?'))
    print('Your current balance is', currbal + depvalue)
    qustion = input('Are you done?')
    if qustion == yes:
        print('Thank you!')


