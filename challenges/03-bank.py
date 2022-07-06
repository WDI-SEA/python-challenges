print("Welcome to Chase bank.")

balance = 4000
transaction = input('What would you like to do? (deposit, withdraw, check_balance)\n')
if (transaction == 'check_balance'):
    print('your balance is ', balance)
trans_amount = input(f"how much would you like to {transaction}\n")
trans_amount = int(trans_amount)
if (transaction == 'deposit'):
    print('your new balance is:', balance + trans_amount)
if (transaction == 'withdraw'):
    print('your new balance is:', balance - trans_amount)
print("Have a nice day!")

