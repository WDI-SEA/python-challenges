

print("Welcome to Chase bank.")

balance = 5000
print("your current balance is", balance)

ask = input('Do you want to do? balance, deposit, withdraw\n')
if (ask == 'balance'):
    print('your balance is', balance)
elif(ask == 'deposit'):
    deposit = input('How much do you want to deposit?\n')
    newBalance = (int(deposit) + balance)
    print("your new balance is ", newBalance)    
else:
    withdraw = input('How much do you want to withdraw?\n')
    newBalance = (balance - int(widthdraw))
    print("your new balance is ", newBalance)
    

print("Have a nice day!")


