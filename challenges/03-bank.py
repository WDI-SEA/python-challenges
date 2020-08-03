print("Welcome to Chase bank.")

# balance to hold to hold variable
done = "no"
transaction = 0
balance = 0

# conditional to execute correct calculation
def bank():
    global balance
    global transaction
    global done

    # used while loop from HW review to actually have this continuously run instead of my calc code reuse
    while True:
    # prompt transactions
        transaction_type = input("What transaction would you like to do: check balance, withdrawal, or deposit?\n")
        if transaction_type == "check balance":
            print("Your current balance is {}".format(balance))
        elif transaction_type == "withdrawal":
            transaction = int(input("How much would you like to {}? \n".format(transaction_type)))
            print("{}-{}= ".format(balance, transaction))
            print(balance-transaction)
        elif transaction_type == "deposit":
            transaction = int(input("How much would you like to {}? \n".format(transaction_type)))
            print("{}+{}=".format(balance, transaction))
            print(balance+transaction)
        else:
            print("there was an error with your transaction!")
        
        done = input("are you done? yes or no\n")
        if done == "yes":
            print("Thanks for your business!")
            break

bank()