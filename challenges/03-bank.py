print("Welcome to Chase bank.")
print("Have a nice day!")

def bank(method):
  mny_balance = 0
  if method == 'deposit':
    add_num1 = int(input('how much would you like to deposit?\n'))
    print(add_num1 + mny_balance)
  elif method == 'withdraw':
    sub_num1 = int(input('how much would you like to withdraw?\n'))
    print(mny_balance - sub_num1)
  elif method == 'balance':
    print(mny_balance)
  else:
    print('wut?')


print(bank(input('what would you like to do, balance, deposit, withdraw?\n')))
