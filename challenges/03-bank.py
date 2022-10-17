print("Welcome to Chase bank.")

running = True
balance = 0

while running:
  print('Would you like to deposit, withdraw, or see your account balance? Type "Cancel" to exit at anytime')
  display = input('Choice: ')

  if display.upper() == 'CANCEL':
    running = False
  if display.upper() == 'EXIT':
    running = False

  if display.upper() == 'DEPOSIT':
    print('How much would you like to deposit today?')
    amount = input('$')
    if amount.upper() != 'CANCEL':
      balance += int(amount)
      
    print('Thank you for your deposit. Will that be all for today?')
    display = input('Choice: ')
    if display.upper() == 'YES':
      running = False 

  if display.upper() == 'WITHDRAW':
    print('How much would you like to withdraw today?')
    amount = input('$')
    if amount.upper() != 'CANCEL':
      balance -= int(amount)

    print('Thank you for your withdrawal. Will that be all for today?')
    display = input('Choice: ')
    if display.upper() == 'YES':
      running = False 

  if display.upper() == 'ACCOUNT BALANCE':
    print(f'Your Account has ${balance}')

    print('Thank you for choosing Chase Bank. Will that be all for today?')
    display = input('Choice: ')
    if display.upper() == 'YES':
      running = False 

print("Have a nice day!")

