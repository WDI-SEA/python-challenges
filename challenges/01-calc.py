# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

method = input("What calculation would you like to do? (add, sub, mult, div) ")

user_num1 = int(input("What is your first number? "))

user_num2 = int(input("What is  your second number? "))

# print(user_num1, user_num2, method)

def determine_method(num1, num2):
    if method == "add":
        return num1 + num2
    elif method == "sub":
        return num1 - num2
    elif method == "mult":
        return num1 * num2
    elif method == "div":
        return num1 / num2
    else:
        print("Invalid calculation")

print(f"Your result is {determine_method(user_num1, user_num2)}")

