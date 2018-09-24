balance = 0

def deposit(amount):
	global balance
	balance += amount
	return balance

def withdraw(amount):
	global balance 
	balance -= amount
	return balance

def check_balance():
	global balance
	return balance

print("Select operation.")
print("1.Deposit")
print("2.Withdraw")
print("3.Check_balance")

choice = input("Enter choice(1/2/3):")

amount = int(input("Enter amount: "))

if choice == "1":
	print(amount,"+",balance,"=", deposit(amount))

elif choice == "2":
	print(amount,"-",balance,"=", withdraw(amount))

elif choice == "3":
	print(check_balance())

else:
	print("Invalid input")