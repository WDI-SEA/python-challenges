print("Welcome to Chase bank.")

# user prompt
transaction_type = input("What transaction would you like to do: check balance, withdrawal, or deposit?\n")

# balance to hold to hold variable
balance = int(2000)

# conditional to execute correct calculation
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