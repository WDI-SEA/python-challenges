print("Welcome to Chase bank.")
print("Have a nice day!")
​
done = "no"
balance = 1000
dollars = 0
​
def atm():
    global done
    global balance
    global dollars
​
​
    #### approach #1 using while loop and if/elif logic ####
    while(done != "yes"):
        response = input("What would you like to do at this atm?\n")
​
        if (response == "balance"):
            print(f"Your balance is {balance}\n")
            done = input("Are you done? Yes or no\n")
        elif (response == "withdraw"):
            dollars = int(input("How much to withdraw?\n"))
            balance = balance - dollars
            print(f"Your balance is {balance}\n")
            done = input("Are you done? Yes or no\n")
        elif (response == "deposit"):
            dollars = int(input("How much to deposit?\n"))
            balance = balance + dollars
            print(f"Your balance is {balance}\n")
            done = input("Are you done? Yes or no\n")