# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calculator():
    operation = input("Which calculation would you like to do? (add, sub, mult, div) ")
    num1 = float(input("what is number 1? "))
    num2 = float(input("what is number 2? "))

    if operation == 'add':
        result = num1 + num2
    elif operation == 'sub':
        result = num1 - num2
    elif operation == 'mult':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "IMPOSSIBLE to divide by ZERO"
    else:
        return "That wasn't an option... (add, sub, mult, div)"
    return f"Your result is {result}."

print(calculator())