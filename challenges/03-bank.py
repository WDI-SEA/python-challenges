print("Welcome to Chase bank.")
print("Have a nice day!")

balance = input("Your current balance is\n")
balance = int(balance)
action = input("What would you like to do? (deposit, withdraw, check_balance)\n")
if action == "deposit":
    deposit_amount = input("How much would you like to deposit?\n")
    deposit_amount = int(deposit_amount)
    new_balance = balance + deposit_amount
    print("Your current balance is " + str(new_balance))
elif action == "withdraw":
    withdraw_amount = input("How much would you like to withdraw?\n")
    withdraw_amount = int(withdraw_amount)
    new_balance = balance - withdraw_amount
    print("Your current balance is " + str(new_balance))
elif action == "check_balance":
    print("Your current balance is " + str(balance))