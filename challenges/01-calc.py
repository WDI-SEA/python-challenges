# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

num1 = int(input("Enter number 1:"))

op = input('Enter operator:')

num2 = int(input('Enter number 2: '))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*" or op == "x":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)