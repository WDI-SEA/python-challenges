
def welcome():
    transaction = ''
    balance = 1000
    print("Welcome to Chase bank.")
    userInput = input('What would you like to do? (deposit, withdraw, check_balance)')
    transaction = userInput
    if transaction == 'deposit':
        toDeposit = input('How much would you like to deposit?')
        balance += int(toDeposit)
        print(f"Your current balance is {balance}")
    elif transaction == 'withdraw':
        toWithdraw = input('How much would you like to withdraw?')
        balance -= int(toWithdraw)
        print(f"Here's your cash. Your current balance is {balance}")
    elif transaction == 'check_balance':
        print(f'Your current balance is {balance}')

welcome()
print("Have a nice day!")