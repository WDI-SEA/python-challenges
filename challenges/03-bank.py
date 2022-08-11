print("Welcome to Chase bank.")

atm = input("Would you Like To: (view_balance, withdrawal, deposit)\n")


global balance
balance = 4000


if atm == "view_balance" or atm == "VIEW_BALANCE":
    print (f'Your balance is $ {balance} ')
if atm == 'withdrawal' or atm =='WITHDRAWAL':
    withdrawal = input("Enter the amount you would like to withdraw?\n")
    balance = balance - int(withdrawal)
    print(f"Your balance after withdrawal is $ {balance}")
if atm == 'deposit' or atm =='DEPOSIT':
    deposit = input("Enter the amount you'd like to deposit?\n")
    balance = balance + int(deposit)
    print(f'Your balance after deposit is $ {balance}')

print("Have a nice day!")
