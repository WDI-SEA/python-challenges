# print("Welcome to Chase bank.")
# print("Have a nice day!")

# balance = 1000
# done = "no"

# def atm():
#     global balance
#     global done

#     while (done != "yes"):
#         ans = input("what would you like to do?\n")

#         if (ans == "deposit"):
#             amount = int(input("How much would you like to deposit?\n"))
#             balance = balance + amount
#             print(f"Your current balance is {balance}\n")
#             done = input("Are you done?\n")
#         elif (ans == "withdraw"):
#             amount = int(input("How much would you like to withdraw?\n"))
#             balance = balance - amount
#             print(f"Your current balance is {balance}\n")
#             done = input("Are you done?\n")
#         elif (ans == "balance"):
#             print (f"Your current balance is {balance}\n")
#             done = input("Are you done?\n")
# atm()        

print("Welcome to Chase bank.")

should_run = True
balance = 0

while should_run:
    print(f"your current balance: {balance}")

    print("what would you liek to do? (deposit, withdraw, check_balance)")

    prompt = "> "
    action = input(prompt)

    if action == "deposit":
        print('enter an amount')
        amount = int(input(prompt))
        balance += amount
    elif action == "withdraw":
        print('enter an amount')
        amount = int(input(prompt))
        balance -= amount
    elif action == "check_balance":
        print(f'your current balance is: {balance}')
    
    print('are you like done or whatever (yes/no)')
    done = input(prompt)
    if done == 'yes':
        should_run: False
    


print("Have a nice day!")