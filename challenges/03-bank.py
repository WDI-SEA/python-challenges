print("Welcome to Chase bank.")
session = True
account = 0
keep_session = True

while session == True:
    operation = input("What would you like to do? (deposit, withdraw, check balance) ")

    if (operation == "deposit"):
        num1 = input("Deposit quantity ")
        num1 = int(num1)
        account = account + num1
        print("Your account is now  {}".format(account))

    elif (operation == "withdraw"):
        num2 = input("Withdraw quantity ")
        num2 = int(num2)
        account = account - num2
        print("Your account is now  {}".format(account))

    elif (operation == "check balance"):
        print("your balance is {}".format(account))

    else:
        print("that operation does not exist!!")



    while keep_session == True:

        new_operation = input("something else ? ")
        if (new_operation == "yes"):
            session = True
            keep_session = False
        elif (new_operation == "no"):
            session = False
            keep_session = False
        else:
            print("Yes or No?? ... Try again")

print("Have a nice day!")
