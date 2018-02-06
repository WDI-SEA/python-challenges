# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# what calculation would you like to do? (add, sub, mult, div)
# add
# what is num 1?
# input
# what is num 2?
# input
# result

def calculator():
    operator = input("Enter +, -, *, or /: ").format(c)
    print(operator)
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))
    # answer = num1 operator num2
    # print(answer)
calculator()