# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


method = input("What operator would you like to use?: ")
num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))


def calculator(method, number1, number2):
    result = 0
    if method == "+":
        print(f"Your result is {number1 + number2}")
    if method == "-":
        print(f"Your result is {number1 - number2}")
    if method == "*":
        print(f"Your result is {number1 * number2}")
    if method == "/":
        print(f"Your result is {number1 / number2}") 

calculator(method, num1, num2)