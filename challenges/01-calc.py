

some_operation = input("please enter an operator: ")
num1 = input("please enter a number:" )
num2 = input("please enter a number2: ")

if some_operation == 'add':
    print(f"the sum of {num1} and {num2} is {int(num1) + int(num2)}" )

elif some_operation == 'subtract':
    print(f"the difference of {num1} and {num2} is {int(num1) - int(num2)}" )

elif some_operation == 'multiply':
    print(f"the product of {num1} and {num2} is {int(num1) * int(num2)}" )

elif some_operation == 'divide':
    print(f"the quotient of {num1} and {num2} is {int(num1) / int(num2)}" )

else: print("invalid operation")

