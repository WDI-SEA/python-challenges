# Write a BankAccount class.

# Bank accounts should be created with the kind of account (like "savings" or "checking").
# Each account should keep track of it's current balance.
# Each account should have access to a deposit and a withdraw method.
# Each account should start with a balance set to zero.
# return the amount withdrawn, for convenience
# Create a checking account and a savings account. Withdraw money from the savings account and deposit that amount into the checking account.
# Bonus: start each account with an additional overdraft_fees property that starts at zero. If a call to withdraw ends with the balance below zero then overdraft_fees should be incremented by twenty.



# class BankAccount():
# 	def __init__(self, kind):
# 		self.balance = 0
# 		self.kind = kind
# 		print('You have created a new {} account!'.format(kind))

# 	def deposit(self, amount):
# 		self.balance += amount
# 		print('You have deposited {}'.format(amount))

# 	def withdraw(self, amount):
# 		self.balance -= amount
# 		print('You have withdrawn {}'.format(amount))

# 	def check_bal(self):
# 		print('You have {}'.format(self.balance))

# checking_acct = BankAccount('checking')
# checking_acct.deposit(4500)
# checking_acct.withdraw(330)
# checking_acct.check_bal()

# Your current balance is
# 4000
# What would you like to do? (deposit, withdraw, check_balance)
# deposit
# How much would you like to deposit?
# 1000
# Your current balance is 5000
# Are you done?
# yes
# Thank you!

class BankAccount():
	def __init__(self):
		self.balance = 0

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		self.balance -= amount

	def check_balance(self):
		print('Your current balance is ${}'.format(self.balance))

my_account = BankAccount()

def use_account():
	# print('Your current balance is: {}'.format(my_account.balance))
	choice = input('What would you like to do? (deposit, withdraw, check_balance)\n')
	if (choice == 'deposit'):
		deposit_num = input('How much would you like to deposit?\n')
		my_account.deposit(int(deposit_num))
		print('You have deposited ${}'.format(deposit_num))
	elif (choice == 'withdraw'):
		withdraw_num = input('How much would you like to withdraw?\n')
		my_account.withdraw(int(withdraw_num))
		print('Your have withdrawn ${}'.format(withdraw_num))
	elif (choice == 'check_balance'):
		my_account.check_balance()
	
	choice = input('Are you done? (yes, no)\n')
	if(choice == 'no'):
		use_account()
	
use_account()

print('Thank you!')