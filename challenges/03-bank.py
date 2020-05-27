print("Welcome to Chase bank.")

balance = '5000'

def transact(balance):
    print('Your current balance is')
    print('$' + balance)
    action = input('What would you like to do? (deposit, withdraw, check_balance) ')
    if action == 'deposit':
        deposit = input('How much would you like to deposit? ')
        print('Deposited $' + deposit + ' into your account')
        balance = int(balance) + int(deposit)
    elif action == 'withdraw':
        withdraw = input('How much would you like to withdraw from your account? ')
        print('Withdrew $' + withdraw + ' from your account')
        balance = int(balance) - int(withdraw)
    elif action == 'check_balance':
        balance = balance
    else:
        print('Sorry, we cannot do that')
        return
    print('Your current balance is')
    print(balance)
    done = input('Are you done yet? (yes or no) ')
    if done == 'yes':
        print('Ok!')
    else:
        print('Too bad, next!')
        
transact(balance)

print("Have a nice day!")