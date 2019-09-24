# Create a prompt that asks the user if they would like to display their
# balance, withdraw or deposit. Write three methods to perform these
# calculations and output the result to the user.

print("Welcome to Chase bank.")
balance = 4000
print(f"Your current balance is\n{balance}")

def transaction_process():
    user_balance = balance
    done = False
    while done == False:
        transaction = input("What would you like to do? (deposit, withdraw, check_balance)\n")
        if transaction == "deposit" or "withdraw" or "check_balance":
            handle_transaction(transaction, user_balance)
        else:
            done = False
            return print("Please enter a valid transaction type (deposit, withdraw, check_balance)\n")
        
        another_transaction = input("Are you done? (Y or N)")
        if another_transaction == "Y":
            done = True
            return print("Have a nice day!")
        else:
            done = False

def handle_transaction(transaction_type, balance):
    if transaction_type == "deposit":
        deposit_amount = int(input("How much would you like to deposit?\n"))
        new_balance = balance + deposit_amount
        print(f"Your new balance is {new_balance}")
        return new_balance
    elif transaction_type == "withdraw":
        withdraw_amount = int(input("How much would you like to withdraw?\n"))
        new_balance = balance - withdraw_amount
        print(f"Your new balance is {new_balance}")
        return new_balance
    elif transaction_type == "check_balance":
        print(f"Your balance is {balance}")
        return balance

transaction_process()

