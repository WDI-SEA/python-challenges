print("Welcome to Chase bank.")
inp1 = input('What would you like to do today? ')

balance = 50

if inp1 == 'check_balance':
    def check_balance():
        print(f"Your current balance is: {balance}")
    check_balance()

elif inp1 == 'withdraw':
    def withdraw():
        withdrawal = input('How much would you like to withdraw?: ')
        withdrawal = float(withdrawal)
        new_balance = balance - withdrawal
        print(f"Your remaining balance is: {new_balance}")
    withdraw()


elif inp1 == 'deposit':
    def deposit():
        deposit = input('How much would you like to deposit?: ')
        deposit = float(deposit)
        new_balance = balance + deposit
        print(f"Your new balance is: {new_balance} ")
    deposit()

print("Have a nice day!")
