print("Welcome to Chase bank.")
print("Have a nice day!")

balance_question = input("Would you like to display your balance? (yes or no)\n")
duties = input("Widthdraw or Deposit?\n")
current_balance = 5000

if (balance_question.lower() == 'yes'):
    print("Your current balance is\n", current_balance)