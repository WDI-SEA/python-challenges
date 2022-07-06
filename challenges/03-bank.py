print("Welcome to Chase bank.")
done = "no"
balance = 4000

def atm():
    global done
    global balance

    while(done != "yes"):
        response = input('What would you like to do? (deposit, withdraw, check_balance)\n') 
        
        if (response == "check_balance"):
            print(f'Your current balance is {balance}')
            done = input("Are you done? Yes or no\n")
        elif (response == "withdraw"):
            dollars = int(input("How much would you like to withdraw?\n"))
            balance = balance - dollars
            print(f"Your balance is {balance}")
            done = input("Are you done? Yes or no\n")
        elif (response == "deposit"):
            dollars = int(input("How much would you like to deposit?\n"))
            balance = balance + dollars
            print(f"Your balance is {balance}")
            done = input("Are you done? Yes or no\n")



print(atm())
print("Have a nice day!")