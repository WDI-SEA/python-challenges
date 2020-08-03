amount = 30
at_bank = True
 
while at_bank:
    actions = input("What would you like to do? withdraw, deposit, check balance, flirt with teller\n")
    if not actions:
        break
    if actions == "deposit":
        deposit = int(input("How much will you deposit? "))
        amount += deposit
        print(f"You deposited an amount of ${deposit}.")
        print(f"Your balance is ${amount}.")
    elif actions == "withdraw":
        withdraw = int(input("How much will you withdraw? "))
        amount -= withdraw
        print(f"You withdrew an amount of ${withdraw}.")
        print(f"Your balance is ${amount}.")
    elif actions == "check balance":
        print(f"Your balance is ${amount}.")
    elif actions == "flirt with teller":
        print("I'm flattered, but this is inappropriate.")
    else:
        at_bank = False

