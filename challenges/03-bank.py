print("Welcome to Chase bank.")
balance = 4000
print('your balance is' , balance)
action = input('what action would like?: ')
amount = float(input('what amount?: '))

if action == 'deposit':
    balance = balance + amount
    print(balance)
if action == 'withdraw'
    balance = balance - amount
    print(balance)

print("Have a nice day!")
