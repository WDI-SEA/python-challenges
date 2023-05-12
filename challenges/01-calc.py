# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


user_input = input("what method wouls you like to use: +, -, *, / ")
user_input_num_1 = input("give me a number")
user_input_num_2 = input('give me another number')
number1 = int(user_input_num_1)
number2 = int(user_input_num_2)

def do_math():
    if user_input == "+":
        return number1 + number2
    elif user_input == "-":
        return number1 - number2
    elif user_input == "*":
        return number1 * number2
    elif user_input == "/":
        return number1 / number2
    else:
        return "not a valid operator"

print(do_math())

