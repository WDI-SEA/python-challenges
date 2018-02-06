print("Welcome to Chase bank.")
ACTION_MSG = "What would you like to do? Type: deposit, withdraw, check_balance\n"
user_action = input(ACTION_MSG)
balance = 4000

if(user_action == "deposit"):
	deposit_amount = int(input("How much would you like to deposit? Include the full number with no $\n"))
	balance += deposit_amount
	print(f"Your new balance is ${balance}")
elif(user_action == "withdraw"):
	withdraw_amount = int(input("How much would you like to withdraw? Include the full number with no $\n"))
	balance -= withdraw_amount
	print(f"Your new balance is ${balance}")
elif(user_action == "check_balance"):
	print(f"Your balance is ${balance}")
else:
	print("Sorry, we do not understand your command")

user_action = input("Have you completed your transaction? Type yes or no\n")
if(user_action == "yes"):
	print("Have a nice day!")
else:
	print("Too bad!")
