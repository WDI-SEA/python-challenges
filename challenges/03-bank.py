# def banking():
#     sampleBalance = 4000
#     is_logged_in = False
#     while is_logged_in == False:
#         print("Welcome to Chase bank.")
#     print('What would you like to do?(deposit, withdraw, check_balance')
#     clientSelection = input()

#     if clientSelection == 'check_balance':
#         print('Your current balance is:\n', sampleBalance)
#         banking()
#         is_logged_in = True
    
# banking()

# print("Have a nice day!")
class Banking(object):
    sample_balance = 4000
    
    def getBalance(self):
        return self.sample_balance

    def deposit(self, deposit_amount):
        self.deposit_amount = deposit_amount
        self.sample_balance += self.deposit_amount
    
    def withdraw(self, withdrawn_amount):
        self.withdrawn_amount = withdrawn_amount
        self.sample_balance -= self.withdrawn_amount
bank_teller = Banking()
while True:
    client_input = input('What would you like to do?\n(deposit, withdraw, check_balance)\n')
    if client_input == 'check_balance':
        print('Your current balance is\n', bank_teller.getBalance())
    elif client_input == 'deposit':
        deposit_amount = int(input('How much would you like to deposit?'))
        bank_teller.deposit(deposit_amount)
        print('Your current balance is\n', bank_teller.getBalance())
        exit_client = input('Are you done?(y/n)')
        if exit_client == 'y':
            break
        else:
            continue
    elif client_input == 'withdraw':
        withdrawn_amount = int(input('How much would like you to withdraw?'))
        bank_teller.withdraw(withdrawn_amount)
        print('Your current balance is now \n', bank_teller.getBalance())


