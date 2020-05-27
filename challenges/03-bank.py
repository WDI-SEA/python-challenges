def deposit(balance):
    newBalance = balance + int(input("How much would you like to deposit?\n"))
    print(f"New Balance: {newBalance}")
    return newBalance
def withdraw(balance):
    newBalance = balance - int(input("How much would you like to withdraw?\n"))
    print(f"New Balance: {newBalance}")
    return newBalance
def check_balance(balance):
    print(f"Current Balance: {balance}")
    return balance
transactions = {
    'deposit':deposit,
    'withdraw':withdraw,
    'check_balance':check_balance
}

def transaction(balance):
    transactionType = input("What would you like to do? (deposit, withdraw, check_balance)\n")
    balance = transactions[transactionType](balance)
    
    areDone = input("Are you done?\n")
    if(areDone == 'no' or areDone == 'n'): transaction(balance)
    return balance

def banking():
    balance = 0
    print(f"Welcome to Chase Bank. Your balance is {balance}")
    transaction(balance)
    print("Have a nice day!")


banking()