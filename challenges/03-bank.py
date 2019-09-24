
balance = 4000
exit = False
print(f'Welcome to Chaste Bank. Your current balance is ${balance}.')


while exit == False:
  action = input('What would you like to do next? ([d]eposit, [w]ithdrawel, check_[b]alance, e[x]it):\n')

  if action == 'deposit' or action == 'd':
    amt = int(input('How much?\n'))
    balance = balance + amt
    print(f'Your new balance is ${balance}.\n')
  elif action == 'withdrawel' or action == 'w':
    amt = int(input('How much?\n'))
    balance = balance - amt
    print(f'Your new balance is ${balance}.\n')
  elif action == 'check_balance' or action == 'b':
    print(f'Your current balance is ${balance}.\n')
  elif action == 'exit' or action == 'x':
    print("Have a nice day!")
    exit = True
  else:
    print(f'Unknown action. Please try again.')
