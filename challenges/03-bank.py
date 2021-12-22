balance = 4000
choice = 'check_balance'
delta = 0
go_on = True
print("Welcome to Chase bank.")
print('Your current balance is:')
print(balance)
while go_on:
  choice = input('What would you like to do? (deposit, withdraw, check_balance)\n')
  if choice == 'withdraw':
    delta = int(input('How much would you like to withdraw?\n'))
    balance -= delta
  elif choice == 'deposit':
    delta = int(input('How much would you like to deposit?\n'))
    balance += delta
  print('Your current balance is:')
  print(balance)
  go_on = input('Are you done?\n')!='yes'
print("Have a nice day!")