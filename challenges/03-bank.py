def new_request():
  while True:
    user_input = input("\nCan we help with anything else? ")
    if (user_input.lower() in ["yes", "y"]):
      return get_action()
    else:
      print("\nHave a nice day!")
      return None

def print_balance(balance):
  print("Your current balance is ", balance)

def get_action():
  while True:
    action = input("\nWhat can we help you with? (balance, withdraw, deposit): ")
    if(action.lower() in ["balance", "withdraw", "deposit"]): return action.lower()
    print("I'm sorry, I don't know how to help with that. Please say 'balance', 'withdraw', or 'deposit'")

def deposit(starting_balance):
  while True:
    try:
      amount_str = input("How much would you like to deposit? ")
      amount = int(amount_str)
      new_balance = starting_balance + amount
      print_balance(new_balance)
      return new_balance
    except:
      print("Invalid amount. Please try again.")

def withdraw(starting_balance):
  while True:
    try:
      amount_str = input("How much would you like to withdraw? ")
      amount = int(amount_str)
      new_balance = starting_balance - amount
      if (new_balance < 0):
        print("I'm sorry. You don't have enough money to withdraw that amount.")
        return starting_balance
      print_balance(new_balance)
      return new_balance
    except:
      print("Invalid amount. Please try again.\n")



print("Welcome to Chase bank.\n")

balance = 4000
print_balance(balance)
action = get_action()

while action != None:
  if action == "balance":
    print_balance(balance)
  elif action == "withdraw":
    balance = withdraw(balance)
  elif action == "deposit":
    balance = deposit(balance)
  
  action = new_request()







