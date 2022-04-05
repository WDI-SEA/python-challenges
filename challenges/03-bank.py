

#age = input("How old are you?\n")
#age = int(age)
print("Welcome to Chase bank.")


def atm():
    done = "no"
    balance = 4000
    while (done != 'yes'):
        ans = input("What would you like to do today?\n")

        if (ans == 'deposit'):
            amount = int(input('How much to deposit?\n'))
            balance = balance + amount
            print(f'Your current balance is{balance}\n')
            done = input("Are you done?\n")
        elif (ans == 'withdrawl'):
            amount = int(input("how much would you like to withdraw?\n"))
            balance = balance - amount
            print(f"your current balance is {balance}\n")
            done = input('are you done?\n')




atm()
print("Have a nice day!")