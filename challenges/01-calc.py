# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operation = input("what calculation would you like to do? (add, sub, mult, div):")
print(operation)
num1 = int(input("First Number:"))
num2 = int(input("Second Number:"))

def calculation(operation,num1,num2):
    if operation == "add":
        total = num1 + num2
    elif operation == "sub":
        total = num1 - num2
    elif operation == "mult":
        total = num1 * num2
    elif operation == "div":
        total = num1 / num2
    else: 
        return "invalid operation"
    return total

print(calculation(operation,num1,num2))
