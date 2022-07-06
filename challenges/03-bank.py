print("Welcome to Chase bank.")

done = "no"
balance = 1000

def atm():
    global done
    global balance

    while(done != "yes"):

        response = input("What would you like to do? (display balance, withdraw, deposit)\n")

        if(response == "display balance"):
            print("Your current balance is", balance)
            done = input("Are you done? yes or no\n")
        elif(response == "withdraw"):
            withdrawal = int(input("How much would you like to withdraw?\n"))
            balance = balance - withdrawal
            print("Your current balance is", balance)
            done = input("Are you done? yes or no\n")
        elif(response == "deposit"):
            deposit = int(input("How much would you like to deposit?\n"))
            balance = balance + deposit
            print("Your current balance is", balance)
            done = input("Are you done? yes or no\n")
print(atm())

print("Have a nice day!")

