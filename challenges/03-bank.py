print("Welcome to Chase bank.")
print("Have a nice day!")


action = input("Chose an action: balance, withdraw, deposit\n" )
user_balance = 4000

if action == 'balance':
    print(user_balance)
elif action == "withdraw":
    deposit = input("how much would you like to withdraw \n")
    deposit_value = int(deposit)
    print(user_balance - deposit_value)
elif action == 'deposit':
    withdraw = input("how much would you like to deposit \n")
    withdraw_amount = int(withdraw)
    print(user_balance + withdraw_amount)
else:
    print("invalid option")




