balance = 20000
print("Welcome to Chase bank.")

command = input("what would you like to do?(see_balance, deposit, withdraw)")

def handle_input(command):
	if command == "see_balance":
		check(balance)
	elif command == "deposit":
		deposit(balance)
	elif command == "withdraw":
		withdraw(balance)
	else:
		print("sorry, try a different command")
		command = input("what would you like to do?(see_balance, deposit, withdraw)")
		handle_input(command)			
	

def check(balance):
	print(balance)
	new_task()

def deposit(balance):
	money= int(input("How much would you like to deposit?"))
	balance += money
	print("Your new balance is", balance)
	new_task()

def withdraw(balance):
	money= int(input("How much would you like to withdraw?"))
	balance -= money
	print("Your new balance is", balance)	
	new_task()

def new_task():	
	next = input("Would you like another transaction?(y/n)")
	if next == "y":
		command = input("what would you like to do?(see_balance, deposit, withdraw)")
		handle_input(command)
	else:	
		print("Have a nice day!")	

handle_input(command)