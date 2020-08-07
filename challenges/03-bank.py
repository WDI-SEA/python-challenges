print("Welcome to Chase bank.")

balance = 1000
done = "no"

def atm():
  # Get a user's balance
  global balance
  global done
  
  # run indefinitely until user declares done = yes
  while (done != "yes"):
    # check user input and see what they would like to do
    ans = input("What would you like to do? \n")

    if (ans == "deposit"):
      # ask user how much they would like to deposit
      # add desposit to balance
      # check if done = yes
      amount = int(input("How much would you like to deposit?\n"))
      balance = balance + amount
      done = input("are you done?\n")
      # if done = yes, goodbye message
      if (done == "yes"):
        print("Thank you! Have a nice day. ")

    elif (ans == "withdraw"):
      # ask user how much they would like to withdraw
      # subtract withdraw to balance
      # check if done = yes
      amount = int(input("How much would you like to withdraw?\n"))
      balance = balance - amount
      done = input("Are you done?\n")
      if (done == "yes"):
        print("Thank you! Have a nice day. ")

    elif (ans == "balance"):
      # show balance and check if done = yes
      print(f"Your current balance is {balance}.\n")
      
      done = input("are you done?\n")
      if (done == "yes"):
        print("Thank you! Have a nice day. ")
    
atm() 