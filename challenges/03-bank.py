print("Welcome to Your Mom bank.")

should_run = True
balance = 0

while should_run:
     print(f"your current balance is: {balance}")

     print("what would you like to do? (deposit, withdraw, check_balance)")
     prompt = "> "
     action = input(prompt)

     if action == 'deposit':
          print('enter an amount')
          amount = int(input(prompt))
          balance += amount
     elif action == 'withdraw':
          print('enter an amount')
          amount = int(input(prompt))
          balance -= amount
     elif action == 'check_balance':
          print(f'your current balance is: {balance}')
     else:
          print(f'choice {action} is not valid, please try again')

     print('Need another transaction? (y/n)')
     done = input(prompt)
     if done == 'n':
          should_run = False


print("Have a nice day!")

