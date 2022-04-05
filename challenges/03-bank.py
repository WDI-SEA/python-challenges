balance = 0
print("Welcome to Chase bank.")
next_transaction = input('what would you like to do: (deposit, withdraw, check_balance)')
if next_transaction == 'deposit':
    deposit_amount = input('how much would you like to deposit')
    print(f'total balance is now {balance + int(deposit_amount)}')
elif next_transaction == 'withdraw':
    withdraw_amount = input('how much would you like to withdraw')
    print(f'total balance is now {balance + int(withdraw_amount)}')
elif next_transaction == 'check_balance':
    print('balance is: {balance}')
print("Have a nice day!")

