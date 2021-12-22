# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


operation = input("What method would you like to use: addition, subtraction, multiplication, or division?")
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

if operation == "add":
    print(f"Answer: {num1 + num2}")
elif operation == "subtraction":
    print(f"Answer: {num1 - num2}")
elif operation == "multiplication":
    print(f"Answer: {num1 * num2}")
elif operation == "division":
    print(f"Answer: {num1 / num2}")
