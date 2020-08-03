balance = 1000
done = "no"

print("Welcome to Chase bank.")
print("Have a nice day!")

def atm():
  global balance
  global done

  while done != "yes"
    ans = input("What would you like to do?\n")

    if ans == "deposit":
      amount = int(input("How much would you like to depposit?\n"))
      balance = balance + amount
      done = input("Are you done?\n")
    elif ans == "withdraw":
      amount = int(input("How much would you like to withdraw?\n"))
      balance = balance - amount
      done = input("Are you done")
    elif ans == "balance":
      print(f"Your current balance is ${balance}.\n")
      done = input("Are you done?\n")
atm()