print("Welcome to Chase bank.")

user = input("What would you like to do? (deposit, withdraw, check_balance)")
balance = 1000
def done_or_not():
	done = input("are you done?")
	if(done == "yes"):
		print("Have a nice day!")
	else: 
		print("What you wanna do now then")
if(user == 'check_balance'):
	print("your current balance is", balance)
	done_or_not()
elif(user == 'deposit'):
	deposit = input("How much you gonna deposit?")
	deposit_amount = int(deposit)
	balance = balance+deposit_amount
	print("your current balance is", balance)
	done_or_not()
else:
	withdraw = input("How much you taking out??")
	withdraw_amount = int(withdraw)
	balance = balance - withdraw_amount
	print("your current balance is", balance)
	done_or_not()