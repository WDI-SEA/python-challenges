class BankAccount():
    def __init__(self, kind):
        self.kind = kind
        self.balance = 0
        self.overdraft_fees = 0

    def deposit(self, deposit):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
        #check and see if I have overdrafted
        if (self.balance < 0):
            self.overdraft_fees += 20
        return amount

# savings = BankAccount('savings')
# checkings = BankAccount('checking')

# pay_check = 200
# savings.deposit(pay_check)

# print('My new balance for savings' + str(savings.balance))
# print('My new checking balance is ' + str(checking.balance))

class Savings(BankAccount):
    pass

