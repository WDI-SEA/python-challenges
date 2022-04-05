# print("Welcome to Chase bank.")
# print("Have a nice day!")

yourbalance = 1000
prompt = '>'
stillbanking = True

while stillbanking:
    print('if you would like to see your balance: 1')
    print('if you would like to deposit: 2')
    print('if you would like to withdraw: 3')
    print('if you would like to stop nanking: 4')

    method = input(prompt)

    if method == '1':
        print(yourbalance)
    elif method =='2':
        print('enter amount')
        yourbalance = int(input(prompt))
        yourbalance =+ yourbalance
        print(f'your balance current is: {yourbalance}')
    elif method == '3':
        print('enter amount')
        print = int(input(prompt))
        yourbalance -= yourbalanceprint
        print(f'your balance current is: {yourbalance}')
    elif method =='4':
        stillbanking = False
    else:
        print('you push wrong button')

print("Have a nice day!")




