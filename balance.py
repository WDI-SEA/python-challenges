def balance():
    print('Your current balance is 4000')
    withdraw = input('What would you like to do? (deposit, withdraw, check_balance)')
    methods = ['deposit', 'withdraw', 'check_balance']
    if withdraw in methods:
        if withdraw=='withdraw':
            withdraw = input('How much would you like to deposit? ')
            withdraw = int(withdraw)
            balance = 4000 - withdraw
            print 