current_balance = 4000
question = input("would like to display your balance, withdraw or deposit?\n")


def bank():
  
  if question == "balance":
    print(f'Your current balance is {current_balance}')

  elif question == "withdraw":
      amount_minus = input("How much would you like to withdraw?\n")
      amount = current_balance - int(amount_minus)
      print(f'Your current balance is now {amount}')

  elif question == "deposit":
      amount_plus = input("How much would you like to deposit?\n")
      total = current_balance + int(amount_minus)
      print(f'Your current balance is now {total}')


def done():
  end = input("are you done?\n")
  if end == "yes":
    print("Have a nice day!")
  elif end == "no":
    question = input("would like to display your balance, withdraw or deposit?\n")
    bank()

    
if question == "balance" or "withdraw" or "deposit":
    bank()
    done()
