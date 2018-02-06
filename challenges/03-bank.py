import random
print("Welcome to Chase bank.")
print("Have a nice day!")
user_ballance = random.randint(5000,10000)
print('Your ballance is {0}.'.format(user_ballance))

def handle_transaction(ballance):
  action = input('What would you like to do? (deposit, withdraw check_balance): ')
  
  if(action == 'deposit'):
    deposit_amt = input('How much would you like to deposit? : ')
    try:
      deposit_amt = int(deposit_amt)
    except:
      print('Please enter a valid number')
    ballance += deposit_amt
    print('Your current ballance is : {0}'.format(ballance))
    done = input('Are you done with the transaction? (yes, no) :')
    if(done == 'no'):
      handle_transaction(ballance)
    else:
      print('Thank you for using our ATM.')

  elif (action == 'withdraw'):
    withdraw_amt = input('How much would you like to withdraw? : ')
    try:
      withdraw_amt = int(withdraw_amt)
    except:
      print('Please enter a valid number')
    ballance -= withdraw_amt
    print('Your current ballance is : {0}'.format(ballance))
    done = input('Are you done with the transaction? (yes, no) :')
    if(done == 'no'):
      handle_transaction(ballance)
    else:
      print('Thank you for using our ATM.')
      
  elif (action == 'check_balance'):
    print('Your current ballance is {0}'.format(ballance)) 
    done = input('Are you done with the transaction? (yes, no) :')
    if(done == 'no'):
      handle_transaction(ballance)
    else:
      print('Thank you for using our ATM.') 
  else:
    print('Please enter a valid selection')
    handle_transaction(ballance)

handle_transaction(user_ballance)
