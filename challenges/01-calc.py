# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

#Defining my functions here for each of the arithmitic 
def add(x, y):
    return x + y

def subtract (x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

#Ask the user to choose a specific operator to do their math
operator = input("Which operation did you want to do?(+,-,*,%):")
x = int(input(('Enter a number: ')))
y = int(input(('Enter another number: ')))

if operator == '+':
    print(x,"+",y,"=", add(x,y))

if operator == '-':
    print(x,"-",y,"=", subtract(x,y))

if operator == '*':
    print(x,"*",y,"=", multiply(x,y))

if operator == '%':
    print(x,"/",y,"=", divide(x,y))
#basic error handling if user didn't choose one of the operators
else:
    print("Unexpected response, choose one of the following operators +, -, *, %")
