print("Welcome to Chase bank.")
print("Have a nice day!")

done = "no"
balance = 1000
dollars = 0

def atm():
    global done
    global balance
    global dollars

    #### approach #1 using while loop and if/elif logic ####
    # while(done != "yes"):
    #     response = input("What would you like to do at this atm?\n")

    #     if (response == "balance"):
    #         print(f"Your balance is {balance}\n")
    #         done = input("Are you done? Yes or no\n")
    #     elif (response == "withdraw"):
    #         dollars = int(input("How much to withdraw?\n"))
    #         balance = balance - dollars
    #         print(f"Your balance is {balance}\n")
    #         done = input("Are you done? Yes or no\n")
    #     elif (response == "deposit"):
    #         dollars = int(input("How much to deposit?\n"))
    #         balance = balance + dollars
    #         print(f"Your balance is {balance}\n")
    #         done = input("Are you done? Yes or no\n")
    #### end approach #1 ####
    
    #### approach #2 using dictionary and conditional logic == INCOMPLETE, doesn't effect global balance ####
    transactions = {
        "balance": balance,
        "withdraw": balance - dollars,
        "deposit": balance + dollars
    }

    while(done != "yes"):
        action = input("What would you like to do at this atm?\n")
        if(action == "withdraw" or action == "deposit"):
            dollars = int(input(f"How much would you like to {action}?\n"))
            balance = transactions[action]
        if (action in transactions):
            balance = transactions[action]
            print(f"Your current balance is {balance}")
            done = input("Are you done? Yes or no\n")
        else:
            return print("not a valid transaction, try again!")
    #### end approach #2 ####

print(atm())

# def service():
#     transaction = input(
#         'What would you like to do? (deposit, withdraw, check_balance)')
#     print(transaction)
#     if transaction == 'check_balance':
#         print('Your current Balance is', balance)
#     elif transaction == 'deposit' or 'withdraw':
#         amount = input(f'How much would you like to {transaction}?')
#     print(amount)
