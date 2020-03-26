print("Welcome to Chase bank.")
print("Would you like to access your balance, withdraw, or deposit (enter balance, withdraw, or deposit)?")
user_action = input()
balance = 2000

def balance_func():
  print(f"You have {balance} in your account.")


def withdraw_func():
  print("How much would you like to withdraw?")
  withdraw_amt = int(input())
  new_balance = balance - withdraw_amt
  print(f"You have withdrawn {withdraw_amt} and have {new_balance} remaining in your account.")

def deposit_func():
  print("How much would you like to deposit?")
  deposit_amt = int(input())
  new_balance = deposit_amt + balance
  print(f"You have deposited {deposit_amt} and now have {new_balance} in your account.")



if user_action == "balance":
  balance_func()

elif user_action == "withdraw":
  withdraw_func()

elif user_action == "deposit":
  deposit_func()


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