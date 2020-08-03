print("Welcome to Chase bank.")
print("Have a nice day!")

def deposit(x, y):
  return x + y

def withdraw(x, y):
  return x - y

def check_balance(x):
  return x


def bankTransaction():
  bankAction = input("What would you like to do? (deposit, withdraw, check_balance")
  if bankAction in ('deposit', 'withdraw', 'check_balance'):
    currentBalance = int("4000")
    if bankAction == 'deposit':
      depositAmount = int(input('How much would you like to deposit?'))
      print("Your current balance is ", deposit(currentBalance, depositAmount))
      areYouDone()
    elif bankAction == 'withdraw':
      withdrawalAmount = int(input("How much would you like to withdraw?"))
      print("Your current balance is ", withdraw(currentBalance, withdrawalAmount))
      areYouDone()
    elif bankAction == 'check_balance':
      print("your current balance is ", currentBalance)
      areYouDone()
  else 
    print("Invalid Input")

def areYouDone():
  finished = input("Are you done? (yes, no)")
  if finished in ('yes', 'no'):
    if finished == 'yes':
      print("Thank you!")
    elif finished == 'no':
      bankTransaction()

bankTransaction()
