
print("Welcome to Chase bank.")

age = int(input("What is your age? "))

if (age): 
    bank_acct = 5000
    print(f"Your balance is {bank_acct}")
    answ = input("Would you like to: (deposit, withdraw, check_balance, quit_application)? ")
    if (answ == "deposit"):
        x = int(input("Deposit: "))
        bank_acct = x + bank_acct
        print(f"Thanks for your business! Your balance is {bank_acct}.")
    elif(answ == "withdraw"):
        x = int(input("Withdraw: "))
        if(x > bank_acct):
            prompt = input("Sorry, you do not have sufficient funds, try again? ")
        else: 
            bank_acct = bank_acct - x
            prompt = input(f"Thanks for your business! Your balance is {bank_acct}. Would you like to make another transaction?")
    elif(answ == "check_balance"):
        prompt = input(f"Your balance is {bank_acct}. Would you like to make another transaction?")


print("Have a nice day!")

