balance = 4000
done = False

# increase balance by input value
def deposit(balance):
    user_input = input("How much would you like to deposit? ")
    balance += int(user_input)
    check_balance(balance)
    return balance

# decrease balance by input value
def withdraw(balance):
    user_input = input("How much would you like to withdraw? ")
    balance -= int(user_input)
    if balance >= 0:
        check_balance(balance)
    else:
        balance += int(user_input)
        print(f"Insufficient funds, you only have a balance of: {balance}")
    return balance
    
# print balance
def check_balance(balance):
    print(f"Your balance is {balance}")
    return balance

# look up which function to call 
actions = {
    "deposit": deposit,
    "withdraw": withdraw,
    "check_balance": check_balance
}

# the keys in actions are lower case without spaces
def transform(user_input):
    user_input = user_input.lower()
    user_input = user_input.strip()
    return user_input

# read instructions from user
def get_user_action():
    action = transform(input("What would you like to do? (deposit, withdraw, check_balance)"))
    if action in actions:
        return action
    else:
        return None

# perform user reques
def perform_user_action(balance):
    p_action = get_user_action()
    if p_action == None:
        perform_user_action(balance)
    else:
        balance = actions[p_action](balance)
    return balance

def ask_if_done():
    user_input = input("Are you done?")
    if "y" in user_input:
        return True
    return False

print("Welcome to Chase bank.")
print("Have a nice day!")
check_balance(balance)

# ask for input as long as user is not done
while not done:
    balance = perform_user_action(int(balance))
    done = ask_if_done()