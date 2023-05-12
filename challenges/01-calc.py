# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
user_input = input("Please enter a number: ")
if user_input.isdigit():
    number = int(user_input)
else:
    print("That was not a valid number.")
    exit()
result = number + 5
print("The result is:", result)