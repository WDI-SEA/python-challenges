import random

print("Welcome to Chase bank.")
print("Have a nice day!")

user_account_balance = random.randint(100, 56000)

def display_balance():
  global user_account_balance
  print("Your current balance is " + str(user_account_balance))

def withdraw_amount(amount):
  global user_account_balance
  user_num = float(amount)
  if (user_num < user_account_balance):
    user_account_balance -= user_num
  else:
    print("I'm sorry, you don't have that amount in your account.")
  
    display_balance()
  

def deposit_amount(amount):
  global user_account_balance
  user_num = float(amount)

  user_account_balance += user_num
  display_balance()


completed = False

while(completed == False):
  user_input = input("What would you like to do? (deposit, withdraw, check balance)")
  if (user_input == "check balance"):
    display_balance()
  elif (user_input == "deposit"):
    amount_wanted = input("What would you like to deposit?")
    deposit_amount(amount_wanted)
  elif(user_input == "withdraw"):
    amount_wanted = input("What would you like to withdraw?")
    withdraw_amount(user_input)
  else:
    print("Not a valid interaction")
  
  finished_input = input("Anything else?")
  if (finished_input == "no"):
    completed = True

print("Have a nice day!")