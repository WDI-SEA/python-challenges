print("Welcome to Chase bank.")
print("Have a nice day!")

balance = 100
done = "no"
def the_bank():
    global balance
    global done
    while (done != "yes"):
        action = input("What would you like to do?\n")

        if (action == "deposit"):
            amount = int(input("How much would you like to deposit?\n"))
            balance = balance + amount
            print(f"Your new balance is {balance}\n")
            done = input("Are you done with this transaction?\n")
        elif (action == "withdraw"):
            amount = int(input("How much would you like to withdraw?\n"))
            balance = balance - amount
            print(f"Your new balance is {balance}\n")
        elif (action == "balance"):
            print(f"Your current balance is {balance}\n")
            done = input("Are you done with this transaction?\n")
the_bank()