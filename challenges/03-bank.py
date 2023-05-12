print("Welcome to Chase bank.")
print("Have a nice day!")

balance = input("Your current balance is\n")
process = input("What would you like to do?\n")

if process == "deposit":
    question = input("How much would you like to deposit?\n")
    balance = int(balance) + int(question)
elif process == "withdraw":
    question = input("How much would you like to withdraw? \n")
    balance = int(balance) - int(question)

print(f"Your current balance is {balance}")