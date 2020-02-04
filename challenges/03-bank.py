balance = 5000

print("Welcome to Chase bank.")
choice = input('What would you like to do? check_balance, withdraw, or deposit ')
if choice == 'check_balance':
    print(balance)
elif choice == 'withdraw':
    withdraw = int(input('How much would you like to withdraw? '))
    print(balance - withdraw)
elif choice == 'deposit':
    deposit = int(input('How much would you like to deposit? '))
    print(balance + deposit)

print("Have a nice day!")

