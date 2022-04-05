print("Welcome to Chase bank.")

def bank_transaction():
  balance = 4000
  print(f'The current balance is {balance}')
  user_input= input('Would you like to withdraw, deposit, or check_balance?\n')

  if user_input=='check_balance':
    print(f'Your current balance is {balance}')
  elif user_input=='withdraw':
    withdraw = input('How much would you like to withdraw? \n')
    balance -= int(withdraw)
    print(f'After the withdrawl, your balance is currently {balance}')
  elif user_input=='deposit':
    deposit= input('How much would you like to deposit?\n')
    balance += int(deposit)
    print(f'After the depsoit, your current balance is {balance}')
  else:
    print('invalid entry')

  complete = input('Would you like to make another transaction? (yes/no):\n ')
  
  if complete == 'no':
    print('Thank you, have a wonderful day!')
  elif complete == 'yes':
    bank_transaction()

bank_transaction()







