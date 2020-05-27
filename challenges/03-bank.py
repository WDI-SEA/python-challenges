balance = 1000
done = 'no'

print("Welcome to Chase bank.")
while done == 'no':
    txn = input("What would you like to do? (deposit, withdraw, balance)\n")

    if txn == 'deposit':
        deposit = input('How much would you like to deposit? \n')
        balance = int(deposit) + int(balance)
        print("Your new balance is ", balance)
    elif txn == 'withdraw':
        withdrawl = int(input('How much would you like to withdraw? \n')) 
        if withdrawl > balance:
            print("Sorry, you have exceeded your balance.")
        else: 
            balance = int(deposit) - int(balance)
            print("Your new balance is ", balance)
    elif txn == 'balance':
        print("Your balance is ", balance)
    done = input("Are you done with your transactions? (yes/no) \n")
print('Have a nice day!')