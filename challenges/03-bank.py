print("Welcome to Chase bank.")
print("Have a nice day!")

balance = 1000
done = "no"

def atm():
    # get a users balance
    global balance
    global done
    
    # run indefinintely until user declares done
    while (done != "yes"):
        # check user input and see what they want to do
        ans = input("What would you like to want to do?\n")

    
        # user input to act accordingly
        if (ans == "deposit"): 
            # ask user how much they want to deposit
            amount = int(input("How much would you like to deposit?\n"))
            # add deposit to balance
            balance = balance + amount
            # check and see if done 
            done = input("Are you done?\n")

        elif (ans == "withdraw"):
            amount = int(input("How much would you like to withdraw?\n"))
            balance = balance - amount
            done = input("Are you done?\n")
        
        elif (ans == "balance"):
            print(f"Your current balance is {balance}.\n")
            done = input("Are you done?\n")

atm()
    #  