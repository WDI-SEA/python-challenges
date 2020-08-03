print("Welcome to Chase bank.")
print("Have a nice day!")

##GLOBAL VARIABLES
balance = 0
name = ""


##FUNCTIONS
def nextTransaction(): 
    global name

    print(f'Would you like to make another transaction, {name} (yes/no)? ')
    userChoice = input()
    if userChoice == 'yes':
        transaction()
    if userChoice == 'no':
        quit()
    else:
        print('error in input, please try again.')
        nextTransaction()

def transaction():
    global balance

    print('Please enter your name: ')

    name = input()

    print(f"Hello, {name}. Please enter transaction type (balance, deposit, withdraw): ")

    mode = input()


    print(f'transaction type: *{mode}*')

    if mode == "balance":
        # global balance
        print(f'Your current balance is {balance}...')
    elif mode == "deposit":
        print(f'Hello, {name}, please enter an amount to deposit: $')
        deposit = input()
        balance = int(deposit) + balance
        print(f'after depositing ${deposit}, your new balance is {balance}')

    elif mode == "withdraw":
        print(f'Hello, {name}, please enter an amount to withdraw: $')
        withdrawal = input()
        if int(withdrawal) > balance:
            print('error: insufficient funds.')
        elif int(withdrawal) < balance:
            balance = balance - int(withdrawal)
            print(f'After a withdrawal of ${withdrawal}, your balance is ${balance}')
        else:
            print('error in withdrawal transaction')
    else:
        print(f'error in mode selection: {mode} is not recognized by the system')
            
    nextTransaction()

transaction()
