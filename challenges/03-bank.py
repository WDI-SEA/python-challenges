
current_balance = 4000

print('Welcome to Pretty Good Bank!')
action = input("How can I help? You can say 'deposit', 'withdraw', or 'check my balance'.\n")

if action == 'deposit':
    deposit_amount = input('Okay, I can help you with a deposit. How much money would you like to deposit?\n')
    deposit_amount = int(deposit_amount)
    new_balance = current_balance + deposit_amount
    print(f'Gotcha. Your new balance after that {action} is {new_balance}')
elif action == 'withdraw':
    withdraw_amount = input('Okay, I can help you with a withdrawal. How much would you like to withdraw?\n')
    withdraw_amount = int(withdraw_amount)
    new_balance = current_balance - withdraw_amount
    print(f'Done. Your new balance after that {action}al is {new_balance}')
elif action == 'check my balance':
    print(f'You got it. Your current balance is {current_balance}')
else:
    print('Hmm, I don\'t recognize that command.')

final_q = input('Are you all finished? (yes/no)\n')

if final_q == 'yes':
    print('Thanks!')
elif final_q == 'no':
    print('Want to go back to the main menu?')
