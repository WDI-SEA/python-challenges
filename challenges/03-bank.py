
def banking():
    print("Welcome to Chase bank.")
    print("Have a nice day!")

    balance = 4000
    while True:
        print('Your current balance is: ', balance)
        task = input('What do you like to do? (deposit, withdraw, check_balance)')
        if (task == 'deposit'):
            deposit = int(input('How much would you like to deposit?'))
            balance += deposit
        elif (task == 'withdraw'):
            withdraw = int(input('How much would you like to withdraw?'))
            if(withdraw > balance):
                print('Your money is not enough to withdraw')
            else:
                balance -= withdraw
        else:
            balance += 0
        print('Your current balance is: ', balance)
        
        finish = input('Are you done? ')
        if (finish == 'yes'):
            print('Thank you!')
            break;
        else:
            continue
