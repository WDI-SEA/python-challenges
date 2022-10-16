print("Welcome to Chase bank.")
print("Have a nice day!")


initialBalance = 0
runningBalance = 0
i = 0


def setInitialValue():
    global initialBalance
    initialBalance = int(input("Your current balance is:\n"))
    if initialBalance < 0:
        print(f"{initialBalance} is not a sufficient amount")
        setInitialValue()


def transaction():
    global i
    global initialBalance
    global runningBalance

    if i == 0:
        runningBalance = initialBalance

    action = input("What would you like to do? (withdraw, deposit, check_balance)\n")

    if action == "deposit":
        depositAmount = int(input("How much would you like to deposit?\n"))
        runningBalance += depositAmount
        print(f"Your current balance is {runningBalance}")
        i += 1
        return completionRequest()
    elif action == "withdraw":
        withdrawAmount = int(input("How much would you like to withdraw\n"))
        if withdrawAmount > runningBalance:
            print("Insufficient funds")
            i += 1
            return completionRequest()
        else:
            runningBalance -= withdrawAmount
            print(f"Your current balance is {runningBalance}")
            i += 1
            return completionRequest()
    elif action == "check_balance":
        print(f"Your current balance is {runningBalance}")
        i += 1
        return completionRequest()
    else:
        print("Please enter a valid action.")
        i += 1
        return completionRequest()


def completionRequest():
    global runningBalance

    ask = input("Are you done?\n")
    if ask == "Yes" or ask == "yes":
        return print("Thank you!")
    else:
        print(f"Your current balance is {runningBalance}")
        return transaction()


setInitialValue()
transaction()
