print("Welcome to Chase bank.")
balance = 120000


def accounting(action, balance):
    if "deposit" in action:
        deposit = input("How much would you like to deposit?\n")
        balance += int(deposit)
        print(f"Your new balance is {balance}")
        done = input("Are you done?\n")
        sign_out(done, balance)
    elif "withdraw" in action:
        withdrawl = input("How much would you like to withdrawl?\n")
        balance -= int(withdrawl)
        print(f"Your new balance is {balance}")
        done = input("Are you done?\n")
        sign_out(done, balance)
    elif "check_balance" in action:
        print(f"Your balance is {balance}")
        done = input("Are you done?\n")
        sign_out(done, balance)

def sign_out(decision, balance):
    if "yes" in decision:
        pass
    if "no" in decision:
        action = input("What would you like to do? (deposit, withdraw, check_balance)\n")
        accounting(action, balance)


print(f"Your balance is {balance}");
action = input("What would you like to do? (deposit, withdraw, check_balance)\n")
accounting(action, balance)

print("Have a nice day!")