print("Welcome to Chase bank.")

current_balance = 0

print(f'Your current balance is {current_balance}')

def bank_interaction():
    # global current_balance
    print("what would you like to do? (deposit, withdraw, check_balance")
    option = input()
    if option == 'deposit':
        print('How much would you like to deposit')
        deposit_added = input()
        print(f'Your new total is {int(current_balance) + int(deposit_added)}')
        return int(current_balance) + int(deposit_added)
    if option == 'withdraw':
        print('How much would you like to withdraw')
        deposit_subtracted = input()
        print(f'Your new total is {int(current_balance) - int(deposit_subtracted)}')
        return int(current_balance) - int(deposit_subtracted)
    if option == 'check_balance':
        print(f'You currently have {current_balance}')

current_balance = bank_interaction()

print("Are you done? (yes or no)")
answer = input()

if answer == 'yes':
    print("Have a nice day!")
elif answer == 'no':
    print(f'current balance is: {current_balance}')
    bank_interaction()
