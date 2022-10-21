# class CoffeeCup():
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.amount = 0
#     def __str__(self):
#         return f"This {self.capacity}oz coffee cup is {self.amount}oz full."
#     def fill(self):
#         self.amount = self.capacity
#     def drink(self, drink_amount):
#         self.amount -= drink_amount
#         if(self.amount <= 0):
#             self.amount = 0
#     def empty(self):
#         self.amount = 0

# gabes_cup = CoffeeCup(14)
# westons_cup = CoffeeCup(12)
# aprils_cup = CoffeeCup(14)
# zakariahs_cup = CoffeeCup(24)

# gabes_cup.fill()
# print(gabes_cup)
# gabes_cup.empty()
# print(gabes_cup)
# zakariahs_cup.fill()
# print(zakariahs_cup)


import math

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f'{self.x},{self.y}'
#     def distance(self):
#         return math.sqrt(self.x**2 + self.y**2)
    def distance(self, p2):
        dx = self.x - p2.x
        dy = self.y - p2.y
        return math.sqrt(dx**2 + dy**2)

Point.ORIGIN = Point()

p3 = Point(6, 13)
p4 = Point(1,1)
print(p3.distance(p4))

# p0 = Point()
# p1 = Point(3,4)
# print(p1.distance())

# class BankAccount():
#     def __init__(self, acct_type, balance = 0):
#         self.acct_type = acct_type
#         self.balance = balance
#         overdraft_fee = 
#         self.overdraft_fee = overdraft-fee

#     def deposit(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):
#         self.balance -= amount
#         if(self.balance < 0):
#             self.overdraft_fee += 20
#     def __str__(self):
#         return f'This {self.acct_type} account has {self.balance} dollars. Your overdraft fee is: {self.overdraft_fee}'
# gabes_account = BankAccount('checking', 100)
# gabes_account.withdraw(105)
# print(gabes_account)
