
print('Welcome to Pretty Good Bank!')

current_balance = 4000

is_running = True

while is_running:
    action = input("How can I help? You can say 'deposit', 'withdraw', or 'check my balance'.\n> ")
    print(action)

    if action == 'deposit':
        deposit_amount = float(input('Okay, I can help you with a deposit. How much money would you like to deposit?\n~> $'))
        current_balance = current_balance + deposit_amount
        print(f'Gotcha. Your new balance after that deposit is ${current_balance}')
    elif action == 'withdraw' or action == 'withdrawal':
        withdraw_amount = float(input('Okay, I can help you with a withdrawal. How much would you like to withdraw?\n> $'))
        current_balance = current_balance - withdraw_amount
        print(f'Done. Your new balance after that withdrawal is ${current_balance}')
    elif action == 'check my balance' or action == 'check' or action == 'check balance' or action == 'check the balance':
        print(f'Check your balance, you got it. Your current balance is ${current_balance}')
    else:
        print('Hmm, I don\'t recognize that command.')

    final_q = input('Are you all finished? (yes/no)\n> ')

    if final_q == 'yes':
        print('See ya later 🐊')
        is_running = False
    elif final_q == 'no':
        enter = input('Press enter to return to the main menu...')
