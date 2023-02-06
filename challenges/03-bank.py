print("Welcome to Chase bank.")
#age = input("how old are you?\n")
#age = int(age)

# show current balance
current_balance = 4000

def decision_maker():
    decision  = input("What would you like to do? (deposit, withdraw, check_balance) \n")
    if decision == 'deposit':
        deposit =  int(input("How much would you like to deposit? "))
        print("Your current balance is \n", current_balance + deposit) 
 
    elif decision == 'check_balance':
        print('Your current balance is \n', current_balance)
  
    elif decision == 'withdraw':
        withdraw = int(input("How much would you like to withdraw? "))
        if current_balance - withdraw >= 0:
            print("Your current balance is \n", current_balance - withdraw)
        else:
            print("You don't have enough funds.")
 
    else:
        print("Invalid option.")

while True:
    decision_maker()
    done = input("Are you done? (yes/no) ")
    if done == 'yes':
        print("Thank You!")
        break

print("Have a nice day!")

