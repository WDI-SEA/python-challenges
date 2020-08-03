import random

balance = random.randrange(-500, 500, 1)

def chase_bank():
  print("Welcome to Chase bank.")
  main_menu()

def main_menu():
  # greeting message
  print('Main Menu\nWhat would you like to do today? You can deposit money, withdraw money, view your balance or exit the aplication.\nPlease select:\ndeposit\nwithdraw\nbalance\nexit')
  
  # get input from user
  choice = input(':')

  # eval user choice
  if choice == 'exit':
    exit_app()
  elif choice == 'balance':
    view_balance()
  elif choice == 'deposit':
    deposit()
  elif choice == 'withdraw':
    withdraw()
  else:
    print(f'{choice} is not a valid selection, please retry')
    main_menu()

# for user messages
def invalid_number(number):
  print(f'{number} is not a valid number, please retry')

# menu options:
def exit_app():
  print("Have a nice day!")

def view_balance():
  print(f'Your balance is ${balance}')
  if balance < 0:
    print('your account is currently overdrawn and may be subject to fees')
  main_menu()

def deposit():
  # define balance in local scope
  global balance
  # get deposit amount
  amount = input('please enter amount:')

  # return if not a number
  try:
    amount = int(amount)
  except ValueError:
    invalid_number(amount)
    deposit()

  # return if not positive
  if amount < 0: 
    invalid_number(amount)
    deposit()

  # add to balance
  balance += amount
  print(f'${amount} has been added to your balance')

  # apply overdraft fees
  if balance < 0:
    fee = random.randrange(-45, 0, 1)
    balance -= fee
    print(f'your account is overdrawn and subject to a fee of ${fee}')

  # return to main menu
  main_menu()

def withdraw():
  # define balance in local scope
  global balance
  # get withdrawl amount
  amount = input('please enter amount:')

  # return if not a number
  try:
    amount = int(amount)
  except ValueError:
    invalid_number(amount)
    deposit()

  # return if not positive
  if amount < 0: 
    invalid_number(amount)
    deposit()

  # subtract from balance
  balance -= amount
  print(f'${amount} has subtracted added to your balance')

  # apply overdraft fees
  if balance < 0:
    fee = random.randrange(-45, 0, 1)
    balance -= fee
    print(f'your account is overdrawn and subject to a fee of ${fee}')

  # return to main menu
  main_menu()

chase_bank()
