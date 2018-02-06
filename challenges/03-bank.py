print("Welcome to Chase bank.\n How can Chase help you today?")
initial_balance = int(input("Hey also - how much $$ do you wish you had in your account (500000): \n"))

global current_balance
global status

def repeat_interaction(initial_balance):
	current_balance = initial_balance
	status = chase_bank(current_balance)
	while status != "yes":
		status = chase_bank(current_balance)
	print("Have a good day!")


def chase_bank(balance):
	transaction = transaction_type()
	current_balance = transaction_execution(transaction,balance)
	status = user_status()
	return status	


def transaction_type():
	transaction = input("How can Chase help you today? \n Enter one of the following: \n - deposit \n - withdraw \n - check_balance \n ")
	return transaction

def user_status():
	status = input("Are you all done today? \n (yes or no) \n")
	return status

def check_balance(balance):
	print("Your current balance is {0}".format(balance))
	return balance

def deposit(balance):
	amount = int(input("How much would you like to deposit? \n"))
	current_balance = balance+amount

	print("Your new balance is {0}".format((current_balance)))
	return current_balance

def withdraw(balance):
	amount = int(input("How much would you like to withdraw? \n"))
	if(amount > balance):
		print("Sorry - you have insufficient funds")
	else:
		current_balance = balance-amount
		print("Your new balance is {0}".format((current_balance)))
		return current_balance

def transaction_execution(transaction,balance):
	if transaction == "check_balance":
		current_balance = check_balance(balance)
		return current_balance
	elif transaction == "deposit":
		current_balance = deposit(balance)
		return current_balance
	elif transaction == "withdraw":
		current_balance = withdraw(balance)
		return current_balance


repeat_interaction(initial_balance)




