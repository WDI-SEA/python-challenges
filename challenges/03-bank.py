print("Welcome to Chase bank.")



def fdeposit(balance):
	amount = input("How much would you like to deposit\n")
	amount = int(amount) + balance
	return amount
def fwithdraw(balance):
	amount = input("How much would you like to withdraw\n")
	amount = balance - int(amount)
	if(amount < 0):
		print("You do not have the funds to withdraw that amount.")
		return balance
	else :
		return amount







curr_bal = 1000
action = input("What would you like to do? (deposit, withdraw, check_balance)\n")
if(action == "deposit"):
	curr_bal = fdeposit(curr_bal)
	print("Your current balance is " + str(curr_bal))
if(action == "withdraw"):
	curr_bal = fwithdraw(curr_bal)
	print("Your current balance is " + str(curr_bal))
if(action == "check_balance"):
	print("Your current balance is " + str(curr_bal))




print("Have a nice day!")