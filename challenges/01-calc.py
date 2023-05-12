# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


calculation = input("What calculation would you like to do? (add, sub, mult, div): ")

number1 = float(input("What is number 1? "))
number2 = float(input("What is number 2? "))

result = None

if calculation == "add":
    result = number1 + number2
elif calculation == "sub":
    result = number1 - number2
elif calculation == "mult":
    result = number1 * number2
elif calculation == "div":
    if number2 != 0:
        result = number1 / number2
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid calculation method.")

if result is not None:
    print("Your result is", result)
