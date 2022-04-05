print("Welcome to Chase bank.")
print("Have a nice day!")

balance = 100

transaction = input("What would you like to do? (view balance, deposit, withdraw)")

# print(transaction)

if transaction == "view balance" :
    print(f"Your current balance is: {balance}")
elif transaction == "deposit" :
    amount = input("How much would you like to deposit today? ")
    balance += int(amount)
    print(f"Thank you for your deposit. Your current balance is: {balance}.")
elif transaction == "withdraw" :
    amount = input("How much would you like to withdraw today? ")
    balance -= int(amount)
    print(f"Thank you for being an account holder. Your new balance is {balance}")
# else :
#     print(f"Invalid transaction. Please contact your banker.")