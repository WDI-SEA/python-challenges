print("Welcome to Charity bank.")

another_transaction = 'y'
bank_balance = 0.00

def bank_account():
    print('What transaction would you like? (balance, withdrawl, deposit)')
    transaction_type = input()

    def set_another_transaction():
        print('Would you like another transaction (y or n)?')
        global another_transaction
        another_transaction = input()

    def deposit():
        print('How much do you want to deposit?')
        deposit_amount = input()
        global bank_balance
        bank_balance += float(deposit_amount)
        balance()
    
    def withdrawl():
        print('How much do you want to withdrawl?')
        withdrawl_amount = input()
        global bank_balance
        bank_balance -= float(withdrawl_amount)
        balance()
        
    def balance():
        global bank_balance
        print(f'Your current balance is {round(bank_balance,2)}')
        set_another_transaction()

    if transaction_type == 'balance':
        balance()
    elif transaction_type == 'withdrawl':
        withdrawl()
    elif transaction_type == 'deposit':
        deposit()
    
while another_transaction == 'y':
    bank_account()

print("Have a nice day!")

