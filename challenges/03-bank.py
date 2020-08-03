print("Welcome to Chase bank.")
print("Have a nice day!")

def bankTransaction():
    balance = 100
    method = input("Choose your option. [deposit,withdraw,display] : \n")
    if (method == "deposit"):
        value = int(input("How much to deposit? : "))
        balance += value
        print(f"New balance is {balance}")
    elif (method == "withdraw"):
        value = int(input("How much to withdraw? : "))
        balance -= value
        print(f"New balance is {balance}")
    elif (method == "display"):
        print(f"Balance is {balance}")

bankTransaction()

"""
OUTPUT
------
DEPOSIT
Choose your option. [deposit,withdraw,display] :
deposit
How much to deposit? : 500
New balance is 600

WITHDRAW
Choose your option. [deposit,withdraw,display] :
withdraw
How much to withdraw? : 50
New balance is 50

DISPLAY
Choose your option. [deposit,withdraw,display] :
display
Balance is 100

"""