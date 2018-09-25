print("Welcome to Chase bank.")
print("Have a nice day!")

def deposit(dollars):
  new_money = int(input('How much would you like to deposit? '))
  return dollars + new_money

def withdraw(dollars):
  spent = int(input('How much would you like to withdraw? '))
  return dollars - spent

def check_balance(dollars):
  return dollars

balance = int(input('What is your starting balance: '))

request = input('What would you like to do with your money? (withraw, deposit, check_balance) '


if request == 'withdraw':
  print(withdraw(money))
elif request == 'deposit':
  print(deposit(money))
elif request == 'check_balance':
  print(check_balance(money))

