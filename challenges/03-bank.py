print("Welcome to Chase bank.")


balance = 0


def get_balance():
    global balance
    print(" your balance is : $", balance)
    return balance
def withdraw(withdraw_amount):
    global balance
    if withdraw_amount > balance:
        print("insufficient funds")
        return 0
    print("you just withdrew", withdraw_amount)
    balance -= withdraw_amount
    return balance
def deposit(deposit_amount):
    global balance 
    balance =+ deposit_amount
    print("you have deposited" , deposit_amount)

result = input("what would you like to do at Chase bank today ? a. balance b. withdraw c. deposit ")

match result:
    case "a" :
        get_balance()
    case "b":
        withdraw_amount = input("how much would you like to withdraw: ")
        withdraw(int(withdraw_amount))
    case "c":
        deposit_amount = input("how much would you like to deposit: ")
        deposit(int(deposit_amount))

print("Have a nice day!")    