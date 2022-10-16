print("Welcome to Chase bank.")


account_balance = 4000
print('Your current balance is')
print(account_balance)

bank_transaction = input('What would you like to do? (deposit, withdraw, check_balance)\n')

if bank_transaction == 'deposit':
    deposit = input('How much would you like to deposit?\n')
    deposit = int(deposit)
    account_balance += deposit
    print('Your current balance is ' + str(account_balance))
elif bank_transaction == 'withdraw':
    withdraw = input('How much would you like to withdraw?\n')
    withdraw = int(withdraw)
    account_balance -= withdraw
    print('Your current balance is ' + str(account_balance))
else:
    print('Your current balance is ' + str(account_balance))

customer_service = input('Are you done?\n')

if customer_service == 'yes':
    print('Thank you!')
else:
    bank_transaction
print("Have a nice day!")

