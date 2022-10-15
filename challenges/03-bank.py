from typing import final


print("Welcome to Chase bank.")
def transaction(bal):
    print(f'Your current balance is {bal}')
    cust_input = input('What would you like to do? (deposit, withdraw, check_balance)\n')
    if cust_input == "deposit":
        dep_amt = input('How much would you like to deposit?\n')
        bal += int(dep_amt)
        print(f'Thank you for your deposit of ${dep_amt}. Your new balance is ${bal}')
        return bal
    elif cust_input  == "withdraw":
        withdrawl_amt = input("How much would you like to withdraw?\n")
        bal -= int(withdrawl_amt)
        print(f'You have withdrawn ${withdrawl_amt}. Your new balance is ${bal}')
        return
    elif cust_input == "check_balance":
        print(f'Your current balance is {bal}')
        return bal
    else:
        print('I\'m sorry, I don\'t understand.')
        transaction(1000)
transaction(1000)
final_input = input('Is that all for today?(Y/N)\n')
if final_input == 'y':
    print("Have a nice day!")
elif final_input == 'N' or 'n':
    transaction(1000)




