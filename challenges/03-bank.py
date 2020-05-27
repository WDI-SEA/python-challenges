
def puhrompt(balance, donecheck):
        
        action = input('What would you like to do? ')
        amt = input('How much would you like to ' + action + ' $')
        if action == 'deposit':
            balance = balance + int(amt)
        elif action == 'withdraw':
            balance = balance - int(amt)
        print('Your balance is $', balance)
        donecheck = input('Are you done? ')
        while donecheck != 'yes':
            puhrompt(balance, donecheck)
        print('Have a nice day!')
            


def sup(balance):   
    donecheck = 'no'
    print("Welcome to Chase bank.")
    print('Your current balance is ', + balance)
    puhrompt(balance, donecheck)
   

def chaseBank(x):
    
    sup(x)
    

chaseBank(0)