print("Welcome to Chase bank.")
print("Have a nice day!")

balance = 12809
opener = input("balance, withdraw, deposit?")
if opener == 'balance':
    print(balance)
elif opener == 'withdraw':
    print(balance)
    withdraw = input('how much to withdraw')
    withdraw = int(withdraw)
    balance -= withdraw
    print(balance)
elif opener == 'deposit':
    print(balance)
    deposit = input('how much to deposit')
    deposit = int(deposit)
    balance += deposit
    print(balance)
else:
    print('nice try')