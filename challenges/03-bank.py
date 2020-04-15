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


# in class comparison:

# balance = 1000
# done = "no"

# # *lobal variables
# def atm():
#     global balance
#     global done

#     while( done != "yes" ):
#         ans = input("What would you like to do? \n")

#         if (ans == "deposit"):
#             amount = int(input("How much would you like to deposit? \n"))