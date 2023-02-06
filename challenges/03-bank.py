print("Welcome to Chase bank.")
print("Have a nice day!")


# balance = 500

# prompt = input("Would you like to \n 1.Check balance \n 2. Withdraw \n 3. Deposit \n Please select 1, 2 or 3") 

# if prompt == "1":
#     print("Your balance is: ", balance)
# if prompt == "2":
#     withdraw = int(input("How much would you like to withdraw?"))
#     balance = balance - withdraw
#     print("Your balance is: ", balance)
#     print("Please take your $",  withdraw)
# if prompt == "3":
#     deposit = int(input("How much would you like to deposit"))
#     print("Your balance is: ", balance + deposit)
    

###class review
is_running =True

balance = 0

while is_running:
    #do banking
    prompt = " "
    #ask the user what transaction to do
    print("Would you like to \n 1.Check balance \n 2. Withdraw \n 3. Deposit \n Please select 1, 2 or 3")
    transaction = input(prompt)
    # print('user entered: ', transaction)
    #let the user do the transaction
    if transaction == "2":
        withdrawal = input("Amount? ")
        balance -= float(withdrawal)
    elif transaction == "3":
        print("how much?")
        deposit = input(prompt)
        balance += float(deposit)
    elif transaction == "1":
        print("You balance is ", balance)
    else:
        print(f"{transaction} is not a valid transaction")
    #ask the user if they are done
    print("Are you done ? [y/n]")
    is_done = input(prompt)
    if is_done =='y':
        is_running = False

