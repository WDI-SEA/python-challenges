# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operation = input('please enter a operator:')
num1 = input('please input a number:')
num2 = input('please input a number: ')

if operation == 'add':
    print(f"the sums of {num1} and {num2} is {int(num1) + int(num2)}")

elif operation == 'subtract':
    print(f"the difference of {num1} and {num2} is {int(num1) - int(num2)}")

elif operation == 'divide':
    print(f"the division of {num1} and {num2} is {int(num1) / int(num2)}")

elif operation == 'multiply':
    print(f"the product of {num1} and {num2} is {int(num1) * int(num2)}")

else:
    print('no operation WRONG VERY WONG')
