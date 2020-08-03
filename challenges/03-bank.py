print("Welcome to Chase bank.")

balance = 1000
done = "no"

def atm():
    global balance
    global done

    while (done != "yes"):
        ans = input("what would you like to do \n")


    if(ans == "deposit"):
        amount = int(input("How much would you like to deposit? \n"))
        balance = balance + amount 
        done = input("are you done? \n")
    elif(ans == "withdraw"):
        amount = int(input("How much would you like to withdraw? \n"))
        balance = balance - amount
        done = input("are you done? \n")
    elif(ans == "balance"):
        print(f"your current balance is {balance}.\n")
        done = input("are you done?\n")

atm()


