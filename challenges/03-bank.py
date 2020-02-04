print("Welcome to Chase bank.")
print("Have a nice day!")

bank_method = input('What would you like to do today? Enter: display my balance, widthraw, or deposit')

balance = 0
if bank_method == 'display my balance':
    print(f'Your balance is ${balance}')
elif bank_method == 'withdraw':
    withdrawl = int(input('How much would you like to withdraw?'))
    if balance - withdrawl < 0:
        print(f'You don\'t have enough money in your account. Your balance is ${balance}')
    # if balance - withdrawl < 0:
    #     print("You don't have enough money in your account. Your balance is $" + balance)
    else:
        withdrawl = balance - withdrawl
        print(f'You just withdrew ${withdrawl}. Your new balance is ${balance}')
elif bank_method == 'deposit':
    deposit = int(input('How much do you want to deposit?'))
    balance = balance + deposit
    print(f'You just deposited ${deposit}. You new balance is ${balance}')
else:
    print('Inputs not accepted, try again.')