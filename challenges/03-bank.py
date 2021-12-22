print("Welcome to Chase bank.")

balance_question = input(
    "Would you like to display your balance? (yes or no)\n")
current_balance = 5000

def bank_transaction():
    duties = input("Withdraw, Deposit or Check Balance\n")
    if (duties.lower() == 'withdraw'):
        withdraw = int(input('How much woudl you like to withdraw?\n'))
        print('Your new current balance is', current_balance - withdraw)
    elif (duties.lower() == 'deposit'):
        deposit = int(input('How much woudl you like to Deposit?\n'))
        print('Your new current balance is', current_balance + deposit)
    elif (duties.lower() == 'check balance'):
        print(current_balance)


def finished():
    done = input('Are You done?\n')
    if (done.lower() == 'yes'):
        print("Have a nice day!")
    else:
        bank_transaction()


if balance_question.lower() == 'yes':
    print("Your current balance is\n", current_balance)
    bank_transaction()
    finished()
else:
    print("let's continue")
    bank_transaction()
    finished()



