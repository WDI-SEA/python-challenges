
balance = 2000
session = True



def deposit(amount):
  global balance 
  balance += amount
  print(f'your new balance is ${balance}\n')

def withdraw(amount):
  global balance
  if amount <= balance:
    balance -= amount
    print(f'your new balance is {balance}\n')
  else: 
    print(f'no, get a job and make more money')

def check_balance():
  print(f'your current balance is: {balance}\n')

print("Welcome to Chase bank.")

while session:
  op = input('what would you like to do?')

  if op == 'deposit':
    amount = float(input('how much would you like to deposit?\n'))
    deposit(amount)
  elif op == 'withdraw':
    amount = float(input('how much would you like to take out?\n'))
  elif op == "balance":
    check_balance()
  elif op == 'exit':
    session = False
    print("Have a nice day!")





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

