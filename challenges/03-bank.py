balance = 3000

def deposit(balance):
    deposit = float(input('How much would you like to deposit\n'))
    balance = balance + deposit
    print(f"Your new balance is {balance} after your deposit of {deposit}")
    return balance

def check_balance(balance):
    print(f'Your current balance is {balance}')
    return balance

def withdraw(balance):
    withdrawAmt = float(input('how much would you like to withdraw\n'))
    if withdrawAmt > balance:
        print("Insufficient funds for withdrawal")
    else:
        balance = balance - withdrawAmt
    return balance

transactionOp = {
    "1": check_balance,
    "2": deposit,
    "3": withdraw
}

def onlineBanking(balance):
        print("Welcome to Chase bank.")
        print('Your current balance is ',balance)
        banking = input('What would you like to do today: Press 1 for balance, 2 for deposit, 3 for withdraw\n')
        balance = transactionOp[banking](balance)
        continuing = input('would you like to continue y/n\n')
        if continuing == 'y':
            onlineBanking(balance)
       

onlineBanking(balance)

print("Have a nice day!")


