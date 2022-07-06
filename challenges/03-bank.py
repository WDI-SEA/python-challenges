print("Welcome to Chase bank.")
print("What would you like to do today? (display balance, withdraw, deposit)")
action = input()
balance = 5000 

if(action == "display balance"):
    print(balance)
elif(action == "withdraw"):
    num1 = input("Amount to withdraw: ")
    if(int(num1) > int(balance)):
        print("Overdraft alert")
    balance = int(balance) - int(num1)
    print("Your new balance is ", balance)
elif(action == "deposit"):
    num1 = input("Amount to deposit: ")
    balance = int(balance) + int(num1)
    print("Your new balance is ", balance)
else:
    print("Have a nice day!")