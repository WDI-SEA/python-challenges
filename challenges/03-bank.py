balance = 4000
print("Welcome\n")
print("Your current balance is:\n")
print(balance)
operation = input("What would you like to do? (deposit, withdraw, check balance)\n")
if operation == "deposit":
  amount = input("How much would you like to deposit?")
  balance = balance + amount
elif operation == "withdraw":
  amount = input("How much would you like to withdraw?")
  balance = balance - amount
elif operation == "check balance":
  pass
else:
  print("Invalid operation. Please try again.")
print(f"Your balance is {balance}")