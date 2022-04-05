print("Welcome to Chase bank.")
def chase_bank():
    balance = 4000
    print("what would you like to do? (deposit, withdraw, check_balance)")
    user_choice = input()

    if user_choice == "deposit":
        print("How much would you like to deposit?\n")
        deposit = input()
        print(f"Your current balance is: {balance + int(deposit)}")
    elif user_choice == "withdraw":
        print("How much would like to withdraw?\n")
        withdraw = input()
        print(f"Your current balance is: {balance - int(withdraw)}")
    elif user_choice == "check_balance":
        print(f"Your current balance is: {balance}")

    print("Are you done?")
    choice2 = input()

    if choice2 == "yes":
        print("Have a nice day!")
    else:
        print("what would you like to do? (deposit, withdraw, check_balance)")

chase_bank()

