# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def addition(n1,n2):
    return n1+n2

def subtraction(n1,n2):
    return n1-n2

def multiplication(n1,n2):
    return n1*n2

def division(n1,n2):
    if n2 == 0:
       return 'Infinity'
    return n1/n2


operator={
    "add" : addition,
    "sub" : subtraction,
    "mult": multiplication,
    "div" : division
}

def calculator():
   operation= input('What would you like to do: press add, sub, mult, div\n')
   num1 = float(input('Enter your first number '))
   num2 = float(input('Enter your second number '))
   result = operator[operation](num1, num2)
   print(f'The result of {operation} is {result}')

calculator()