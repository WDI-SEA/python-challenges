balance = 20000
done = False

print("Your current balance is", balance)

while not done:
	action = input("What would you like to do? (withdraw, deposit, check_balance)").lower()

	while action not in ["withdraw", "deposit", "check_balance"]:
		action = (input("What would you like to do? (withdraw, deposit, check_balance)"))

	if action == "check_balance":
		print("Your current balance is", balance)
	else:
		amount = None
		while not isinstance(amount, int):
			try:
				amount = int(input("How much would you like to {}?".format(action)))
			except:
				print("This is a bankm take it seriously!")
		if action == "deposit":
			balance += amount
		else:
			balance -= amount

			if balance < 0:
				balance = 0

	response = input("Cool, are you done yet?").lower()

	if response in ["yes", "yeah", "y", "yea", "mhm"]:
		done = True