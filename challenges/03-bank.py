print("Welcome to Chase bank.")

balance = 4000
print('Your current balance is: \n{balance}')
def bank(balance):
    trans = input('what would you like to do?')
    if trans == 'deposit':
        trans_amount = input('How much would you like to deposit \n')
        balance = int(balance) + int(trans_amount)
        print(f'your current balance is: \n{balance}')
    elif trans == 'withdrawl':
        trans_amount = input('How much would you like to withdraw \n')
        balance = int(balance) - int(trans_amount)
        print(f'your current balance is: \n{balance}')
    elif trans == 'check+balance':
        print(f'your current balance is: \n{balance}')
    else:
        print('Invalid transsaction, please try again')
        bank(balance)
bank(balance)

done = input('are you done? (yes/no) \n')
def done_check(done):
    if done == 'no':
        bank(balance)
        done = input('are you done? (yes/no) \n')
        done_check(done)
    else:
        print('haave a nice day')
done_check(done)


print("Have a nice day!")
