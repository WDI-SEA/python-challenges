print("Welcome to Chase bank.")
balance = 1000
running = True

print(f'Your current balance is ${balance}')

while running == True:
    operation = input('Would you like to deposit or withdraw? Enter 1 for deposit or 2 for withdraw: \n')
    
    if operation == '1':
        deposit = int(input('How much would you like to deposit? Enter a number: \n'))
        balance += deposit
    elif operation == '2':
        withdraw = int(input('How much money would you like to withdraw? Enter a number: \n'))
        balance -= withdraw
    else:
        print('Please enter 1 or 2.')
    
    print(f'Your balance is ${balance}.')
    
    want_to_continue = input('Would you like to continue? y/n \n')

    if want_to_continue == 'n':
        running = False
        break

print("Have a nice day!")

