print("Welcome to Chase bank.")
print("Have a nice day!")

ops = input("What would you like to do? (display, withdraw, deposit):\n")
# print(ops)

balance = 5000

if ops == "display":
    print("your balance is" , balance)
if ops == "withdraw":
    print("your balance is" , balance)
    withdrawVal = float(input("how much would you like to withdraw?"))
    balance = balance - withdrawVal
    print("your new balance is", balance)
if ops == "deposit":
    print("your balance is" , balance)
    depositVal = float(input("how much would you like to withdraw?"))
    balance = balance + depositVal
    print("your new balance is", balance)


