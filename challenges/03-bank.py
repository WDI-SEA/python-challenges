balance = 1000
finish = False
def deposit():
    deposit = int(input('How much would you like to deposit?\n'))
    result = balance + deposit
    print(f'Your current balance is {result}')

def widthraw():
    widthraw = int(input('How much would you like to widthraw?\n'))
    result = balance - widthraw
    print(f'Your current balance is {result}')

def check_balance():
    print(f'Your current balance is \n{balance}')

print("Welcome to Chase bank.")
while not finish:
    prompt = input('What would you like to do? (deposit, widthraw, check_balance)\n')
    if prompt == 'deposit':
        deposit()
    elif prompt == 'widthraw':
        widthraw()
    elif prompt == 'check_balance':
        check_balance()
    end_prompt = input('Are you done?\n')
    if end_prompt == 'yes':
        print('Thank you \nHave a good day!')
        finish = True
    elif end_prompt == 'no':
        finish = False
    


