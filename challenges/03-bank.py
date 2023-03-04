print("Welcome to Chase bank.")
print("Have a nice day!")

balance = 4000

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    return balance - amount

print("Your current balance is")
print(balance)


# takes input from customers
transaction = input("What would you like to do? (deposit, withdraw, check_balance)\n")

if transaction == "deposit":
    
    # prompts with questions in new line 
    amount = int(input("How much would you like to deposit?\n"))
    balance = deposit(balance, amount)
    print("Your current balance is", balance)
elif transaction == "withdraw":
    amount = int(input("How much would you like to withdraw?\n"))
    balance = withdraw(balance, amount)
    print("Your current balance is", balance)
elif transaction == "check_balance":
    print("Your current balance is", balance)

done = input("Are you done?\n")

if done == "yes":
    print("Thank you!")




# from hashlib import new


# print("Welcome to Chase bank.")
# print("Have a nice day!")
# session = True
# account = 0


# def new_operation():
#     global session
#     input("something else? (yes, no) \n")
#     if (new_operation == "yes"):
#          session = True      
#     elif (new_operation == "no"):
#          session = False
        

# while session == True:
    
#     operation = input("What would you like to do? (deposit, withdraw, check balance) \n")

#     if (operation == "deposit"):
#         num1 = input("Deposit quantity \n")
#         num1 = int(num1)
#         account = account + num1
#         print(f"Your account is now  {account}")
#         new_operation()

#     elif (operation == "withdraw"):
#         num2 = input("Withdraw quantity \n")
#         num2 = int(num2)
#         account = account - num2
#         print(f"Your account is now  {account}")
#         new_operation()

#     elif (operation == "check balance"):
#         print(f"your balance is {account} \n")
#         new_operation()
#         print(session)


# print("Have a nice day!")