print("Welcome to Chase bank.")
print("Have a nice day!")

balance = 3000

choice = input('What you trynna do? (deposit, withdraw, check_balance) ')

if choice == "deposit":
    dep = input('how much tho? ')
    print(int(dep) + balance)
elif choice == 'withdraw':
    withdraw = input('how much tho?')
    print(balance - int(withdraw))
else:
    print(balance)

