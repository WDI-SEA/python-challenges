print("Welcome to Chase bank.")
print("Have a nice day!")

is_running = True

balance = 0


# def examp():
#     examp()

# examp()

while is_running:
    # do banking
    prompt = '➡️ '
    # ask the user what transaction to do
    print("What kind of banking are you doing? (deposit, withdrawal, check_balance")
    transaction = input(prompt)
    # print('user entered:', transaction)
    # let the user do that transaction
    if transaction == "deposit":
        print("how much?")
        how_much = input(prompt)
        balance += float(how_much)
    elif transaction == "withdrawal":
        print("how much?")
        how_much = input(prompt)
        balance -= float(how_much)
    elif transaction == "check_balance":
        print(f"current balance: {balance}")
    else:
        print(f"{transaction} is not a valid transaction.Lets get it together, user.")

    # ask the user if they are done
    print("are you like done or whatever 🙄 [y/n]")
    is_done = input(prompt)
    if is_done == 'y':
        is_running = False


print("Have a nice day!")
