print("Welcome to Chase bank.")
print("Have a nice day!")

def bank_visit():
    balance = 1000
    bank_questions = input("Balance, withdraw, or deposit?\n")
    if (bank_questions == "Balance"):
        print(f"Your current balance is {balance}")
    if (bank_questions == "withdraw"):
        num = int(input("How much to withdraw?\n"))
        balance = balance - num
        print(f"Your current balance is {balance}")
    if (bank_questions == "deposit"):
        num = int(input("How much to deposit?\n"))
        balance = balance + num
        print(f"Your current balance is {balance}")