print("Welcome to Chase bank.")
print("Have a nice day!")

balance = 4000

def main():
  prompt = input('What would you like to do? (deposit, withdraw, check_balance)\n')
  match prompt:
    case 'deposit':
      deposit()
      check_balance()
    case 'withdraw':
      withdraw()
      check_balance()
    case 'check_balance':
      check_balance()
    case _:
      print('Invalid option selected, please only choose from the listed options')
      main()
  done_check = input('Are you done? (yes, no)\n')
  match done_check:
    case 'no':
      main()
    case 'yes':
      print('Thank you!')
    case _:
      print('Thank you!')
        
def deposit():
  num = int(input('How much would you like to deposit?\n'))
  global balance
  balance = balance + num

def withdraw():
  num = int(input('How much would you like to withdraw?\n'))
  global balance
  balance = balance - num

def check_balance():
  global balance
  print(f'Your current balance is {balance}\n')

main()