global BALANCE
BALANCE = 4000
action = 'deposit'
done = 'no'

def deposit(num):
  global BALANCE
  print('this was the deposit', num)
  BALANCE = BALANCE + int(num)
  print('this is new balance', BALANCE)

def withdraw(num):
  global BALANCE
  print('this was the withdraw', num)
  BALANCE = BALANCE - int(num)
  print('this is new balance', BALANCE)

def check_balance():
  global BALANCE
  print('Your current balance is', BALANCE)

print("Welcome to Chase bank.")
print("Your current balance is")
print(BALANCE)

while(done != 'yes'):
  print("What would you like to do? (deposit, withdraw, check_balance)")
  action = input()
  if(action == 'deposit'):
    print('How much would you like to deposit?')
    deposit(input())
  elif(action == 'withdraw'):
    print('How much would you like to withdraw?')
    withdraw(input())
  elif(action == 'check_balance'):
    check_balance()
  print('Are you done?')
  done = input()


print("Have a nice day!")

