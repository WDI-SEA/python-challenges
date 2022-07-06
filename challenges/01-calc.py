# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calculator():
    math_operation = input('what calculation would you use?  add, sub, mult, or div\n')
 #   print(method)
# these are the inputs that user makes for calculation. Wrapped in Int() as they will be numbers
    num1 = int(input("what is the first number?\n"))
    num2 = int(input("what is the second number?\n"))

#    print(num1, num2)
#Dictionary
    methods = {
        "add": num1 + num2,
        "mult": num1 * num2,
        "div": num1 / num2,
        "sub": num1 - num2
    }

#If in dictionary, perform calc
    if (math_operation in methods):
        return methods[math_operation]
    else: 
        return print('that is not a good math. Try again')

print(calculator())