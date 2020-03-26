# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

calc = input("What calculation would you like to do? ( add, subtract, multiply, divide )\n")
num1 = int(input("What is number 1?\n"))
num2 = int(input("What is number 2?\n"))

if calc.lower() == "add":
    result = num1 + num2
elif calc.lower() == "subtract":
    result = num1 - num2
elif calc.lower() == "mutliply":
    result = num1 * num2
else:
    result = num1 / num2

print("Your result is " + str(result))

