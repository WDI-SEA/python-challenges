print("Welcome to Chase bank.")
def banking():
  bal = 4000
  option = input("What would you like to do? (deposit, withdraw, check_balance) \n")
  if (option == "deposit"):
    a = int(input("Lovely, how much would you like to deposit? \n"))
    bal = bal + a
    print(f"Thank you for your deposit, your new balance is {bal}")
  elif (option == "withdraw"):
    a = int(input("Of course, how much would you like to withdraw? \n"))
    bal = bal - a
    print(f"Thank you for your withdraw, your new balance is {bal}")
  elif (option == "check_balance"):
    print(bal)
  else:
    print("Hmm there seems to be a problem with your request.")
banking()
print("Have a nice day!")