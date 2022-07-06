print("Welcome to Chase bank.")
print("Have a nice day!")

# options = input("What would you like to do? (deposit, withdraw, check_balance)")
# print(options)

# if(options=="deposit"):
#     return int(input("How much would you like to deposit?"))

done = "no"
balance = 1000

def atm():
    global done
    global balance

    while(done != "yes"):
        response = input("What would you like to do?")
        if(response=="balance"):
            print(f"Your balance is {balance}")
            done = input("Are you done? Yes or No")
        elif(response=="withdraw"):
            dollars = int(input("How much to withdraw?"))
            balance = balance-dollars
            print(f"Your balance is {balance}")
            done = input("Are you done? Yes or No")

        elif(response=="deposit")
            dollars = int(input("How much to deposit?"))
            balance = balance+dollars
            print(f"Your balance is {balance}")
            done = input("Are you done? Yes or No")


print(atm())