# Let's be fancy and use functions as dictionary values!

def deposit(balance):
    return balance + int(input("How much? "))
def withdraw(balance):
    amount = int(input("How much? "))
    if amount > balance:
        print ("That would overdraw your account!  Transaction aborted")
        return balance
    else:
        return balance - amount
def view_balance(balance):
    return balance

bankAction = { 'deposit': deposit, 'withdraw': withdraw, 'viewbalance': view_balance }
yes_or_no = {'y': True, 'n': False}

def helpCustomer(balance, finished):
    if finished:
        return None
    else:
        user_request = input("Would you like to 'deposit', 'withdraw', or 'view balance'?")
        balance = bankAction[user_request.replace(" ", "")](balance)
        print ("Your balance is " + str(balance))
        finished = yes_or_no[input("Are you finished? (Y/N) ").lower()]
    helpCustomer(balance, finished)


print("Welcome to Chase bank.")
helpCustomer(0, False)
print("Have a nice day!")