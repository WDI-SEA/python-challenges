# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operations = ['add','sub','mult','div']
def ops(op,x,y):
    return {
        'add': x+y,
        'sub': x-y,
        'mult':x*y,
        'div': x/y
    }[op]

def calc():
    operation = input("What calculation would you like to do? (add, sub, mult, div)\n")
    num1 = int(input("Enter the first value:\n"))
    num2 = int(input("Enter the second value:\n"))
    print("Your result is:")
    print(ops(operation,num1,num2))

calc()


