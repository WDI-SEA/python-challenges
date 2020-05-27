print("Welcome to Chase bank.")
current = 1000
print("current ballance is:", current)
bank = input('what would you like to do today? (deposit or withdraw?):')
if bank == "deposit":
    money = int(input("How much?"))
    print(current + money)
elif bank == "withdraw":
    money = int(input("How much?"))
    print(current - money)


print("Have a nice day!")
