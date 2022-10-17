print("Welcome to Chase bank.")

def transactions(balance):
    print(f'your current balance is {balance}')
    user_input = input("What would you like to do? (deposit, withdraw, check_balance)\n")
    if user_input == "deposit":
        deposit= int(input("How much would are you deposting?\n"))
        balance += (deposit)
        print(f'your new balance is: {balance}')
        return balance
    elif user_input == "withdraw":
        withdraw = int(input("How much would you like to withdraw?\n"))
        balance -= (withdraw)
        print(f'your new balance: is {balance}\n')
        return balance
    elif user_input == "check_balance":
        print(f'your account balance is: {balance}\n')
        return balance
    else:
        print("please enter a valid choice\n")
        transactions(2000)
# transactions(2000)

# signoff = input("will that be all for today? (y/n)?\n")
# if signoff ==  "y" or "Y":
#     print ("Thank You! Have a fantastic day!")
# elif signoff == "n" or "N":
#     transactions(2000)


# ================= review answers ==================
print("Welcome to Chase bank.")

should_run = True
balance = 0

while should_run:
    print(f"your current balance is: {balance}")

    print("what would you like to do? deposit, withdraw, check_balance?")
    prompt = " >"
    action = input(prompt)

    if action == "deposit":
        print("enter an amount")
        amount = int(input(prompt))
        balance += amount
    elif action == "withdraw":
        print("enter an amount")
        amount = int(input(prompt))
        balance -= amount
    elif action == "check_balance":
        print(f"your current balnce is {balance}")
    else:
        print(f"choice{action} is not valid")

print("are you done (y/n)")
done = input(prompt)
if done == "y":
    should_run = False

print("have a nice day")


