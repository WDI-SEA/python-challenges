def getAction():
	action = input("What would you like to do? (deposit, withdraw, check_balance)\n").lower()
	options = ['deposit', 'withdraw', 'check_balance']
	if action in options:
		return action
	else:
		print(action+" is not a valid choice!")
		return getAction()

def getDiff(action):
	try:
		return int(input("How much would you like to "+action+"?\n"))
	except:
		print("Invalid entry: please enter an amount!")
		return getDiff(action)

def giveBalance(balance):
	return "Your current balance is "+str(balance)+"."

def doneYet(bal):
	decision = input("Are you done? (y/n)\n").lower()
	if (decision == "yes") or (decision == "y"):
		return "Thank you!"
	elif (decision == "no") or (decision == "n"):
		return bankTransaction(bal)

def bankTransaction(currBalance):
	bal = currBalance
	print("Welcome to Chase bank!"+giveBalance(bal))
	action = getAction()
	if action == 'deposit':
		diff = getDiff(action)
		bal += diff
		result = "Deposit complete! "
	elif action == 'withdraw':
		diff = getDiff(action)
		bal -= diff
		result = "Withdrawl complete! "
	else:
		result = "Ok. "
	print(result+giveBalance(bal)+"\n")
	doneYet(bal)


print(bankTransaction(4000))
	
