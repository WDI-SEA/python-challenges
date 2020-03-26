
def deposit(num1, num2):
    sum = num1 + num2
    return str(sum)

def withdraw(num1, num2):
    sum = num1 - num2
    return str(sum)

def show_balance(num):
    return str(num)




print("Welcome to Chase bank.")

visit = True

current_balance = 8000

while visit == True:
    transaction = input("What would you like to do? (deposit, withdraw, check-balance)\n")
    if transaction.lower() == "deposit" or transaction.lower() == "withdraw":
        amount = int(input(f"How much would you like to {transaction}?\n"))
        if transaction.lower() == "deposit":
            new_balance = deposit(amount, current_balance)
            print("Your current balance is: " + new_balance)
        else:
            new_balance = withdraw(current_balance, amount)
            print("Your current balance is: " + new_balance)
    else:
        print("Your current balance is: " + show_balance(current_balance))

    end = input("Are you done? (yes/no)\n")

    if end == "yes":
        visit = False
    else:
        current_balance = int(new_balance)


print("Have a nice day!")

