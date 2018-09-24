print("Welcome to Chase bank.")
done = False
balance = 4000
while(done is False):
  action = input("What would you like to do? (deposit, withdraw, check_balance)\n")
  if(action == 'check_balance'):
    print(f'Your balance is {balance}')
  elif(action == 'deposit'):
    try:
      amount = int(input("How much would you like to deposit?\n"))
    except:
      print('That\'s not a valid number.')
    balance += amount
    print(f'Your current balance is {balance}')
  elif(action == 'withdraw'):
    try:
      amount = int(input("How much would you like to withdraw?\n"))
    except:
      print('That\'s not a valid number.')
    if(amount > balance):
      print('Insufficient funds')
    else:
      balance -= amount
      print(f'Your current balance is {balance}')
  else:
    print('Not a valid action.  Please try again')
  moreActions = input('Are you done? (yes, no)\n')
  if(moreActions == 'yes'):
    done = True

print("Have a nice day!")