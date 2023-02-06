# print("Welcome to Chase bank.")
# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
# class Bank_Account:
# 	def __init__(self):
# 		self.balance=5000
# 		input('What would you like to do? (deposit, withdraw, check_balance')
#         if input == 'deposit':
#             self.deposit()
#         elif input == 'withdraw':
#             self.withdraw()
#         elif input == 'check_balance':
#             self.display()

	# def deposit(self):
	# 	amount=float(input("Enter amount to be Deposited: "))
	# 	self.balance += amount
	# 	print("\n Amount Deposited:",amount)

	# def withdraw(self):
	# 	amount = float(input("Enter amount to be Withdrawn: "))
	# 	if self.balance>=amount:
	# 		self.balance-=amount
	# 		print("\n You Withdrew:", amount)
	# 	else:
	# 		print("\n Insufficient balance ")

	# def display(self):
	# 	print("\n Net Available Balance=",self.balance)


# s = Bank_Account()

# s.deposit()
# s.withdraw()
# s.display()

# print("Have a nice day!")



print('Welcome to Chase bank.')
is_running = True
balance = 0
while is_running:
    print('What would you like to do? (deposit, withdraw, check_balance)')
    method = input('>')
    if method == 'deposit':
        print('How much would you like to deposit?')
        amount = input('>')
        balance += int(amount)
        print(f'Your current balance is {balance}')
    elif method == 'withdraw':
        print('How much would you like to withdraw?')
        amount = input('>')
        balance -= int(amount)
        print(f'Your current balance is {balance}')
    elif method == 'check_balance':
        print(f'Your current balance is {balance}')
    else:
        print('Invalid input')
    print('Are you done?')
    is_done = input('>')
    if is_done == 'yes':
        is_running = False
    

print('Have a nice day!')