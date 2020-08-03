print("Welcome to Chase bank.")
print("Have a nice day!")

##GLOBAL VARIABLES
defaultBalance = 0
name = ""
balanceDictionary = {'lou':'50', 'user':'100'}


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
    global name
    global defaultBalance
    global balanceDictionary

    print('Please enter your name: ')

    name = input()

    if name in balanceDictionary:
        print(f'username {name} found... proceeding to mode selection...')
    else:
        print(f'creating user {name} with balance ${defaultBalance}')
        balanceDictionary[name] = defaultBalance
        print(balanceDictionary)

    print(f"Hello, {name}. Please enter transaction type (balance, deposit, withdraw): ")

    mode = input()

    print(f'transaction type: *{mode}*')

    if mode == "balance":
        # global balance
        print(f'Your current balance is ${balanceDictionary[name]}...')
    elif mode == "deposit":
        print(f'Hello, {name}, please enter an amount to deposit: $')
        deposit = input()
        balanceDictionary[name] = int(deposit) + int(balanceDictionary[name])
        print(f'after depositing ${deposit}, your new balance is ${balanceDictionary[name]}')

    elif mode == "withdraw":
        print(f'Hello, {name}, please enter an amount to withdraw: $')
        withdrawal = input()
        if int(withdrawal) > int(balanceDictionary[name]):
            print('error: insufficient funds.')
        elif int(withdrawal) <= int(balanceDictionary[name]):
            balanceDictionary[name] = int(balanceDictionary[name]) - int(withdrawal)
            print(f'After a withdrawal of ${withdrawal}, your balance is ${balanceDictionary[name]}')
        else:
            print('error in withdrawal transaction')
    else:
        print(f'error in mode selection: {mode} is not recognized by the system')
            
    nextTransaction()

transaction()
