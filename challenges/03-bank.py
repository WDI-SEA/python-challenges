print("Welcome to Chase bank.")
print("What would you like to do? (deposit, withdraw, check_balance")
selection = input()
balance = 0

if selection == 'depocit':
    print("How much would you like to deposit?")
    ammount = input()
    balance == balance + int(ammount)
if selection == 'withdtraw':
    print("How much would you like to withdraw?")
    ammount = input()
    balance == balance + int(ammount)
if selection == 'check_balance':
    print("Your balance is : $",balance,".")

