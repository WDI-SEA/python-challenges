print("Welcome to Chase bank.")
# print("Have a nice day!")

curBal = int(input("Your current balance is: "))
whatToDo = input("What would you like to do? (deposit, withdraw, check balance): ")
# deposit = int(input("How much would you like to deposit? "))
# withdrawal = int(input("How much would you like to withdraw? "))
# done = input("Are you done? ")

if whatToDo == "deposit":
    deposit = int(input("How much would you like to deposit? "))
    print (curBal+deposit)
elif whatToDo == "withdraw":
    withdrawal = int(input("How much would you like to withdraw? "))
    print (curBal-withdrawal)
elif whatToDo == "check balance": 
    print(curBal)
# elif done == "yes":
#     print("Thank you!")


# done = "no"
# while done ="no":
#     curBal = int(input("Your current balance is: "))    
#     whatToDo = input("What would you like to do? (deposit, withdraw, check balance): ")
#         if whatToDo == "deposit":
#             deposit = int(input("How much would you like to deposit? "))
#             print (curBal+deposit)
#         elif whatToDo == "withdraw":
#             withdrawal = int(input("How much would you like to withdraw? "))
#             print (curBal-withdrawal)
#         elif whatToDo == "check balance": 
#             print(curBal)



