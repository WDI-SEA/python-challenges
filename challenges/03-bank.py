print("Welcome to Chase bank.")

# Display balance
# Withdraw
# Deposit

balance = 0
option = None

while (option != 4):
    print('Would you like to \n1. View balance \n2. Withdraw \n3. Deposit \n4. Leave')

    option = int(input())

    if option == 1:
        print(f'Balance: {balance}')

    elif option == 2:
        print('How much would you like to withdraw?')
        amount = int(input())
        balance -= amount
        print(f'Withdrew {amount}. Current balance: {balance}')

    elif option == 3:
        print('How much would you like to deposit?')
        amount = int(input())
        balance += amount
        print(f'Deposited {amount}. Current balance: {balance}')

    elif option == 4:
        print("Have a nice day!")

    else:
        print('Please select a valid option from the list')
