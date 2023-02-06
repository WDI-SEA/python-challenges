print("Welcome to Chase bank.")

balance = 0

def deposit():
    print('How much are you depositing?')
    check = input()
    try: 
        check = int(check)
    except:
        print('please input number')
        exit()

    global balance
    balance += check
    print(balance)
    print('Are you finished? (Y/N)')
    answer = input().upper()
    if answer == 'Y':
        print("Have a nice day!")
        exit()
    elif answer == 'N':
        option()
    else:
        print("Have a nice day!")


def withdraw():
    print( f'How much would you like to withdraw?')
    check = input()
    try: 
        check = int(check)
    except:
        print('please input number')
        exit()

    global balance
    balance -= check
    print(balance)
    print('Are you finished? (Y/N)')
    answer = input().upper()
    if answer == 'Y':
        print("Have a nice day!")
        exit()
    elif answer == 'N':
        option()
    else:
        print("Have a nice day!")

def check_balance():
    print( f'Your current balance is {balance}')
    print('Are you finished? (Y/N)')
    answer = input().upper()
    if answer == 'Y':
        print("Have a nice day!")
        exit()
    elif answer == 'N':
        option()
    else:
        print("Have a nice day!")   

def option():
    print( 'What would you like do to? ( Deposit, Withdraw, Check balance )')
    operation = input().lower()
    print(operation)

    if operation == "deposit":
        deposit()
    elif operation == "withdraw":
        withdraw()
    elif operation == "check balance":
        check_balance()
    else:
        print('wrong input')
        option()

option()

