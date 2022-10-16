# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


def calculator():
    question = input("What calculation would you like to do? (add, sub, mult, div)\n")

    firstNum = input("Enter the first number:\n")

    secondNum = input("enter a second number:\n")

    result = ""
    if question == "add":
        result = int(firstNum) + int(secondNum)

    if question == "sub":
        result = int(firstNum) - int(secondNum)

    if question == "mult":
        result = int(firstNum) * int(secondNum)

    if question == "div":
        result = int(firstNum) / int(secondNum)

    return f"Your result is {result}"


print(calculator())
