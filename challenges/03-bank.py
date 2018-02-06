print("Welcome to Chase bank.")
print("Have a nice day!")

def bank():
    total = 4000
    action="q"
    while(action):
        print("Your current balance is\n$",round(total,2))
        action_in = input("What would you like to do? (deposit, withdraw, check_balance)\n")
        action = action_in[0].lower()

        if (action in ["d","w","c"]):
            if(action=="d"):
                amount = input("How much would you like to deposit?")
                total+=float(amount)
            if(action=="w"):
                amount = input("How much would you like to withdraw?")
                if(float(amount)<=total):
                    total-=float(amount)
                else:
                    print("You don't have that amount, peasant!!!!")
            print("Your balance is\n$",round(total,2))

        else:
            action=0

        action = input("Are you done?\n")
        if (action[0].lower()!="n"):
            action=0
bank()
