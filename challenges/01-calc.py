# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


def calculator():
    # Ask for the operation
    operation = input("What do you want to do?(add, sub, mult, div)\n")

    # Ask for the numbers
    num1 = int(input("Num 1?\n"))
    num2 = int(input("Num 2?\n"))

    # Perform the calculation
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
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Error: Invalid operation.")
        return

    # Print the result
    print("Your result is " + str(result))

calculator()
