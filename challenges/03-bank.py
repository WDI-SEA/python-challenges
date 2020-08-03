balance = 1000
done = "no"

print("Welcome to Chase bank.")

def atm():
  # get a user's balance
  global balance
  global done

  # run indefinitely until user declares 'done'
  while (done != "yes"):
    # check user input and see what they want to do
    ans = input("What would you like to do?\n")
    # use user input to act accordingly
    if (ans == "deposit"):
      # ask user how much they want to deposit
      amount = int(input("How much would you like to deposit?\n"))
      # add deposit to balance
      balance = balance + amount
      # check and see if done
      done = input("Are you done?\n")
    elif (ans == "withdraw"):
      amount = int(input("How much would you like to withdraw?\n"))
      balance = balance - amount
      done = input("Are you done?\n")
    elif (ans == "balance"):
      print(f"Your current balnace is {balance}.\n")
      done = input("Are you done?\n")

atm()

print("Have a nice day!")