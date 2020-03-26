balance = 4000
done = False


def deposit():
    user_input = input("How much would you like to deposit? ")
    global balance
    balance += int(user_input)
    check_balance()

def withdraw():
    user_input = input("How much would you like to withdraw? ")
    global balance
    balance -= int(user_input)
    if balance >= 0:
        check_balance()
    else:
        balance += int(user_input)
        print(f"Insufficient funds, you only have a balance of: {balance}")
    balance += int(user_input)
    

def check_balance():
    print(f"Your balance is {balance}")

actions = {
    "deposit": deposit,
    "withdraw": withdraw,
    "check_balance": check_balance
}

def transform(str):
    str = str.lower()
    str = str.strip()
    return str

def get_user_action():
    action = transform(input("What would you like to do? (deposit, withdraw, check_balance)"))
    if action in actions:
        print("Got it")
        return action
    else:
        return None

def perform_user_action():
    p_action = get_user_action()
    actions[p_action]()

def ask_if_done():
    user_input = input("Are you done?")
    if "y" in user_input:
        return True
    return False

print("Welcome to Chase bank.")
print("Have a nice day!")
check_balance()

while not done:
    perform_user_action()
    done = ask_if_done()
