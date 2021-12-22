# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
result = 0
def calculator():
    method = input('Which calculation would you like to perform? (add, sub, mult, div)')
    num1 = input('First Number:')
    num2 = input('Second Number:')
    if method=='add' :
        result = int(num1) + int(num2)
    elif method == 'sub':
        result = int(num1) - int(num2)
    elif method == 'mult':
        result = int(num1) * int(num2)
    elif method == 'div':
        result = int(num1) / int(num2)
    print(f"Your result is {result}")

calculator()