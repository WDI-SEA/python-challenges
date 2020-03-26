# Create a prompt that asks the user if they would like to display their balance, withdraw or deposit. Write three methods to perform these calculations and output the result to the user.

# Gather user input using the input function. Note that input always returns user input as a string. You have to manually convert it to an int or a float to make it behave like number. Also, end the input prompt with a \n newline character if you want the user to type in on the next line.

# age = input("How old are you?\n")
# age = int(age)
# Here is a sample output:

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

myBalance = 4000

def bank(balance):
  print("your current balance is\n", balance)
  print("what would you like to do? (deposit, withdraw, check_balance)")
  action = input()
  if action == "deposit":
    print("How much would you like to deposit?")
    add = int(input())
    balance += add
  elif action == "withdraw":
    print("how much would you like to withdraw?")
    sub = int(input())
    balance -= sub
  print("your current balance is\n", balance)
  

bank(myBalance)