
# challenge one


from audioop import reverse


def calculator():
    operation = input('What calculation would you like to do? (add, sub, mult, div)\n')
    input_one = input('first number\n')
    input_two = input('second number\n')
    if operation == 'add':
        print(int(input_one) + int(input_two))
    if operation == 'sub':
        print(int(input_one) - int(input_two))
    if operation == 'mult':
        print(int(input_one) * int(input_two))
    if operation == 'div':
        print(int(input_one) / int(input_two))

# calculator()

def reverse_string():
    input_string = input('Enter a string:\n')
    answer = ''
    for x in reversed(input_string):
        answer += x
    
    print(answer)

# reverse_string()

def bank_account():
    current_balance = 0
    operation = input('What would you like to do? (deposit, withdraw, check balance) \n')
    if operation == 'deposit':
        deposit = input('How much would you like to deposit? \n')
        current_balance += int(deposit)
        print(f"Your current balance is {current_balance}")
        done = input('Are you finished? (y/n)')
        if done == 'y':
            return
        elif done == 'n':
           bank_account()
    if operation == 'withdraw':
        withdraw = input('How much would you like to withdraw? \n')
        withdraw = int(withdraw)
        if withdraw >= current_balance:
            confirm = input('This could incur an overdraw, would you like to continue? (y/n)')
            if confirm == 'y':
                current_balance -= withdraw
                print(f'Your current balance is {current_balance}')
                done = input('Are you finished? (y/n)')
                if done == 'y':
                    return
                elif done == 'n':
                    bank_account()
            elif confirm == 'n':
                print('Cancelling transaction...')
                done = input('Are you finished? (y/n)')
                if done == 'y':
                    return
                elif done == 'n':
                    bank_account()
        if withdraw < current_balance:
            current_balance -= int(withdraw)
            print(f'Your current balance is {current_balance}')
            done = input('Are you finished? (y/n)')
            if done == 'y':
                return
            elif done == 'n':
                bank_account()
    if operation == 'check balance':
        print(current_balance)
        done = input('Are you finished? (y/n)')
        if done == 'y':
            return
        elif done == 'n':
           bank_account()

# bank_account()


def sort_string():
    doneSorted = ''
    toSort = input('Please enter string. \n')
    for x in sorted(toSort):
        doneSorted += x

    print(doneSorted)

sort_string()

