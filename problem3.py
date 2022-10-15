# Create a prompt that asks the user if they would like to display their balance, withdraw or deposit. Write three methods to perform these calculations and output the result to the user.

# Gather user input using the input function. Note that input always returns user input as a string. You have to manually convert it to an int or a float to make it behave like number. Also, end the input prompt with a \n newline character if you want the user to type in on the next line.

balance = 1000

print(f"Your balance is {balance}")

options = input("Would you like to see your balance, withdraw, or deposit? ")

user_choice = str(options)

print(user_choice)

if user_choice == "balance":
  print(f"Your balance is {balance}")
elif user_choice == "deposit":
  deposit_amount = input("How much money would you like to deposit? ")
  user_deposit = float(deposit_amount)
  print(f"Your balance is now {balance + user_deposit}")
elif user_choice == "withdraw":
  withdraw_amount = input("How much would you like to withdraw? ")
  user_withdraw = float(withdraw_amount)
  print(f"Your balance is now {balance - user_withdraw}")
else:
  print("Please enter valid choice and amount.")
