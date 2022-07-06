from turtle import done


print("Welcome to Chase bank.")
print("Have a nice day!")

# balance = 4000
# print("Your balance is", balance)

# action = input('What would you like to do? (deposit, withdraw, check_balance)\n')

# if(action == 'deposit'):
#     amount = input(f"How much would you like to {action}\n")
#     balance += int(amount)
#     print("Your new balance is", balance)
# elif(action == 'withdraw'):
#     amount = input(f"How much would you like to {action}\n")
#     balance -= int(amount)
#     print("Your new balance is", balance)
# else:
#     print("Your balance is", balance)

dont = 'no'
balance_two = 2000

def atm():
    global done
    global balance_two

    while(done != 'yes'):
        response = input("What would you like to do at this atm?\n")

        if(response  == 'check_balance'):
            print("Your balance is", balance_two)
        elif (response == 'withdraw'):
            amount = int(input(f"How much would you like to {response}\n"))
            balance_two -= amount
            print("Your balance is now", balance_two)
        elif (response == 'deposit'):
            amount = int(input(f"How much would you like to {response}\n"))
            balance_two += amount
            print("Your balance is", balance_two)

print(atm())