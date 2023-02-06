# Create a prompt that asks the user if they would like to display their balance, withdraw or deposit. Write three methods to perform these calculations and output the result to the user.

# Gather user input using the input function. Note that input always returns user input as a string. You have to manually convert it to an int or a float to make it behave like number. Also, end the input prompt with a \n newline character if you want the user to type in on the next line.


print("Welcome to Chase bank.")
print("Have a nice day!")

age = input("How old are you?\n")
age = int(age)

balance = 4000

while age >= 18:
    print("You are old enough to open an account.")
    print("Your current balance is ${}.".format(balance))
    action = input("What would you like to do? (deposit, withdraw, check_balance)\n")
    if action == "deposit":
        deposit = input("How much would you like to deposit?\n")
        deposit = int(deposit)
        balance = balance + deposit
        print("Your current balance is ${}.".format(balance))
        # ask if they want to do another transaction
        proceed = input("Would you like to do another transaction? (y/n)\n")
        if proceed == "y":
            proceed = ""
            continue
        else:
            print("Thank you for banking with us.")
            break

    elif action == "withdraw":
        withdraw = input("How much would you like to withdraw?\n")
        withdraw = int(withdraw)
        balance = balance - withdraw
        print("Your current balance is ${}.".format(balance))
        proceed = input("Would you like to do another transaction? (y/n)\n")
        if proceed == "y":
            proceed = ""
            continue
        else:
            print("Thank you for banking with us.")
            break
    elif action == "check_balance":
        print("Your current balance is ${}.".format(balance))
        proceed = input("Would you like to do another transaction? (y/n)\n")
        if proceed == "y":
            proceed = ""
            continue
        else:
            print("Thank you for banking with us.")
            break
    else:
        print("Invalid action.")
        proceed = input("Would you like to do another transaction? (y/n)\n")
        if proceed == "y":
            proceed = ""
            continue
        else:
            print("Thank you for banking with us.")
            break
else:
    print("You are not old enough to open an account.")

