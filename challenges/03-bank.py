print("Welcome to Chase bank.")

options = input("Would you like to withdraw, deposit, or check_balance? \n")
balance = 2300
balance = int(balance)
deposit = input("how much would you like to deposit?\n")
deposit = int(deposit)
withdraw = input("how much would you like to withdraw?\n")
withdraw = int(withdraw)
response = input("would you like to display your balance?")




def banking():
    if options == "check_balance":
        return balance
    if options == "deposit":
        response
        if response == "yes":
            return f"Thanks for banking with us your balance is {balance + deposit}"
        if response == "no":
            return "thanks for banking with us"
    if options == "withdraw":
        if response == "yes":
            return f"Thanks for banking with us your balance is {balance - withdraw}"
        if response == "no":
            return "thank you"


       
        

    
    
print(banking())


print("Have a nice day!")

