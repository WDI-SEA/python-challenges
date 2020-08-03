# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calc():
    print("What calculation would you like to do? (add, sub, mult, div)")
    user_input = input()
calc()
    user_input_1 = int(input("What is number 1?"))
    user_input_2 = int(input("What is number 2?"))
    if user_input == 'add':
        result = user_input_1 + user_input_2
    elif user_input == 'sub':
        result == user_input_1 - user_input_2
    elif user_input == 'div':
        result == user_input_1 / user_input_2
    elif user_input == 'mult':
        result == user_input_1 * user_input_2
    print(f"Your result is {result}")