# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
def calc_input():
    method = input("Would you like to add, subtract, multiply, or divide?: ")
    num_1 = input("What is the first number?: ")
    num_2 = input("What is the second number?: ")
    if method == 'add':
        answer = int(num_1) + int(num_2)
    elif method == 'subtract':
        answer = int(num_1) - int(num_2)
    elif method == 'multiply':
        answer = int(num_1) * int(num_2)
    elif method == 'divide':
        answer = int(num_1) / int(num_2)

    print(f'Your answer is {answer}')

calc_input()