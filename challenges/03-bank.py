print("Welcome to Chase bank.")
print("Have a nice day!")

def prompt(account):
    balance = 500
    account = input("Do you want to see your balance, withdraw or deposit?")

    if account == 'balance':
        print('Your balance is', balance)
    elif account == 'withdraw':
        withdraw = int(input("How much would you like to withdraw?"))
        if withdraw <= balance:
            balance -= withdraw
        else:
            print("Insufficient balance.")
    elif account == 'deposit':
        deposit = int(input("How much would you like to deposit?"))
        balance += deposit

    return balance

print(prompt("Egor"))
        
        
