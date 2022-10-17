# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
def calculator(operation, num1, num2):
    if operation == 'add':
        res = num1 + num2
    elif operation == 'sub':
        res = num1 - num2
    elif operation == 'mult':
        res = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            res = "Number 2 cannot be 0"
        else:
            res = num1 / num2
    else:
        res = "wrong operation input"
    print("Your result is", res)

operation = input("What calculation would you like to do? (add, sub, mult, div)\n")
number1 = float(input("What is number 1?\n"))
number2 = float(input("What is number 2?\n"))
calculator(operation, number1, number2)