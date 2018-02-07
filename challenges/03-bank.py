print("Welcome to Chase bank.")
def person():
    action = input("what would you like to do?(deposit, withdraw, check_balance): " )
    balance = 2500
    withdraw = int (input('how much to withdraw?'))
    age = input("how much would you like to deposit?")

    if action == 'check_balance':
        print('your balance is', balance)
    elif action == 'withdraw':
        print(withdraw)
        print('your current balance is ')

person()
