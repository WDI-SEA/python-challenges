print("Welcome to Chase bank.")
print("Have a nice day!")



def bank():
	str = input ("Enter your password: \n")
	money = 4000
	
	operation = input ("What would you like to do? (deposit, withdraw, check_balance) \n")

	if operation == 'deposit':
		num = int(input('How much would you like to deposit? \n'))
		new_balance = money + num
		print ('your current balance is {}'.format(new_balance))
	elif operation == 'withdraw':
		num = int(input('How much would you like to withdraw? \n'))
		new_balance = money - num
		print ('your current balance is {}'.format(new_balance))
	elif operation == 'check_balance':
		print(' Your Current Balance is \n {}'.format(money))
	else:
		print('please enter a valid input!')
	again()

def again():
	bank_again = input('Are you done? \n')
	if bank_again.upper() == 'NO':
		bank()
	elif bank_again.upper() == 'YES':
		print ('Thank you!')



bank()