balance = 4000
while True:
  print("Welcome to Chase bank.")
  choice = input("What would you like to do? (deposit, withdraw, check balance)\n").lower()
  if choice == "deposit":
    amount = int(input("How much would you like to deposit?\n"))
    balance += amount
    print(f"Your new balance is ${balance}")
  elif choice == "withdraw":
    amount = int(input("How much would you like to withdraw?\n"))
    balance -= amount
    print(f"Your new balance is ${balance}")
  elif choice == "check balance":
    print(f"Your current balance is ${balance}")
  
  user_input = input("Are you done? Y/n.").lower
  if user_input == "y":
    print("Have a nice day!")
    break


