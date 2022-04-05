print("Welcome to Chase bank.")

balance=4000

transaction = input('would you like to display your balance, withdraw or deposit?: ')



if transaction == 'balance':
    print(f'your balance is ${balance}')
elif transaction== 'withdraw':
    withdrawl = input('how much would you like to withdraw?: ')
    withdrawl= int(withdrawl)
    new_balance = balance - withdrawl
    print(f'after your withdrawl of ${withdrawl}, you have ${new_balance} in your account')
elif transaction == 'deposit':
    deposit = input('how much would you like to deposit?: ')
    deposit= int(deposit)
    new_balance = balance + deposit
    print(f'after your deposit of ${deposit}, you have ${new_balance} in your account')
else :'please select a valid transaction option'

print("Have a nice day!")
