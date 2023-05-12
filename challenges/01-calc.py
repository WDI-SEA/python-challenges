# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


def math(operator, num1, num2):
    # if adding
    if (operator == "add"):
        return num1 + num2
    # else if subtracting 
    elif (operator == "subtract"):
        return num1 - num2 
    # else if multiplying
    elif (operator == "multiply"):
        return num1 * num2
        # num 1 * num 2
    # else 
    elif (operator == "divide"):
        return num1 / num2
        # num 1 / num 2
    else:
        return "try again"


# print(math("divide", 4, 5))
operator = input("What calculation would you like to do?")
num1 = input("What is number 1?")
num2 = input("What is number 2?")
print(math(operator, int(num1), int(num2)))
# math("divide", 8, 2)