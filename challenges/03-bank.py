print("Welcome to Will bank.")

balance = 3000
print("your current balance is", balance)

operator = input("what would you like to do? (deposit, withdraw, check_balance)? ")
if operator == "deposit":
    deposit = input("How much would you like to deposit? ")
    balance = int(deposit) + int(balance)
    print("your new balance is ", balance)
elif operator == 'withdraw':
    withdrawl = int(input("how much would you like to withdraw? ")) 
    if withdrawl > balance:
        print("sorry, you have exceeded your balance. ")
    else: 
        balance = int(deposit) - int(balance)
        print("your new balance is ", balance)
elif operator == "check_balance":
    print("your balance is ", balance)

print('have a nice day come back soon!') 