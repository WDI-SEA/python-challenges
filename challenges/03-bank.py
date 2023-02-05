# print("Welcome to Chase bank.")
# print("Have a nice day!")


def decide(amount,decision):
    if decision == 'deposit':
        deposit(amount)
    elif decision == 'withdraw':
        withdraw(amount)
    else: 
        check_balance(amount)

def deposit(amt):
    deposit_amt = int(input("How much would you like to deposit?\n"))
    check_balance(amt + deposit_amt)
def withdraw(amt):
    withdraw_amt = int(input("How much would you like to withdraw?\n"))
    check_balance(amt - withdraw_amt)
def check_balance(amt):
    again = input(f'Your current balance is {amt}\nAre you done? (yes/no)\n')
    if again == 'no':
        decision = input("What would you like to do? (deposit, withdraw, check_balance)\n")
        decide(amt,decision)

msg = int(input('Your current balance is\n'))
decision = input("What would you like to do? (deposit, withdraw, check_balance)\n")
decide(msg,decision)
