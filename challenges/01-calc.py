# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calculator():
    print("Add, subtract, multiply, or divide?")
    user_input = input()
    first_number = input("What is the first number?")
    second_number = input("What is the second number?")
    if user_input == "Add":
        result = first_number + second_number
    if user_input == "subtract":
        result = first_number - second_number
    if user_input == "multiply":
        result = first_number * second_number
    if user_input == "divide":
        result = first_number / second_number
    print(f"The answer is {result}")

calculator()