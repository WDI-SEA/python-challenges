print("Welcome to Chase bank.")

balance = 500

print(f"Your balance is ${balance}")

answer = input("What would you like to do (withdraw, deposit, check_balance)? ")

if answer == "withdraw":
    answer2 = input("How much would you like to withdraw? ")
    answer2 = int(answer2)
    if answer2 > balance:
        print("Sorry, you do not have enough funds for that transaction")
    else:
        balance = balance - answer2
        print(f"After your withdrawl, you have ${balance} in your account")
if answer == "deposit":
    answer2 = input("How much will you be depositing today? ")
    answer2 = int(answer2)
    balance = balance + answer2
    print(f"After your deposit of ${answer2}, you have an account balance of ${balance}")
if answer == "check_balance":
    print("I literally just told you what your balance is")


print("Have a nice day!")

