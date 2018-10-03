print("Welcome to Chase bank.")
print("Have a nice day!")

balance = 4000

def deposit(amt):
	global balance
	balance += amt
	return balance 

def withdraw(amt):
	global balance
	balance -= amt
	return balance 

def check_balance(amt):
	global balance
	return balance 

choice = input("Enter choice(deposit/withdraw/balance):")
amt = int(input("Enter amount: "))

if choice == 'deposit':
    print(amt, '+', balance, '=', deposit(amt))
elif choice == 'withdraw':
    print(amt, '-', balance, '=', withdraw(amt))
elif choice == 'balance':
    print(check_balance())        
else: 
    print('enter in a valid input')

