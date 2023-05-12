print("Welcome to Chase bank.")

options = input("Would you like to withdraw, deposit, or check_balance? \n")
balance = 2300
balance = int(balance)
num1 = input("how much would you like to deposit?\n")
num1 = int(num1)
num2 = input("how much would you like to withdraw?\n")
num2 = int(num2)
response = input("would you like to display your balance?")




def banking():
    if options == "check_balance":
        return balance
    if options == "deposit":
        response
        if response == "yes":
            return f"Thanks for banking with us your balance is {balance + num1}"
        elif response == "no":
            return "thanks for banking with us"
    if options == "withdraw":
        response
        if response == "yes":
            return f"Thanks for banking with us your balance is {balance - num2}"
        if response == "no":
            return "thank you"


       
        

    
    
print(banking())


print("Have a nice day!")

