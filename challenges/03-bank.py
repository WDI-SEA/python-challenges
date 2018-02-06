print("Welcome to Umpqua")

request = input("What would you like to do? (deposit, withdraw, check_balance)? \n")

def withdraw(current):
	amount = int(input("how much would you like to take out? \n"))
	newbalance = current - amount
	if newbalance >= 0:
		print("your new balance is {}".format(newbalance))
		otherTransaction(newbalance)
	else:
		print("insufficient funds. Your balance is {}".format(current))
		request = input("What would you like to do? (deposit, withdraw, check_balance)? \n")
		evaluateAgain(request, current)

def deposit(current):
	amount = int(input("how much would you like to deposit? \n"))
	newbalance = current + amount
	print("your new balance is {}".format(newbalance))
	otherTransaction(newbalance)

def check_balance(current):
	newbalance = current
	print("your balance is {}".format(newbalance))
	otherTransaction(newbalance)

def evaluate(request):
	current = 4000
	if request == "withdraw":
		balance = withdraw(current)
	elif request == "deposit":
		balance = deposit(current)
	elif request == "check_balance":
		check_balance(current)
	else:
		print("not a valid option")
		request = input("What would you like to do? (deposit, withdraw, check_balance)? \n")
		evaluate(request)

def evaluateAgain(request, current):
	if request == "withdraw":
		balance = withdraw(current)
	elif request == "deposit":
		balance = deposit(current)
	elif request == "check_balance":
		check_balance(current)
	else:
		print("not a valid option")
		request = input("What would you like to do? (deposit, withdraw, check_balance)? \n")
		evaluate(request)

def otherTransaction(newbalance):
	more = input("anything else(yes, no) \n")
	if more == "yes":
		request = input("What would you like to do? (deposit, withdraw, check_balance)? \n")
		current = newbalance
		evaluateAgain(request, current)
	elif more == "no":
		print("Have a nice day!")

evaluate(request)


