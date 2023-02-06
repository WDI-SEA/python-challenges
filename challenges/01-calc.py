# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


# defining arithmetic functions using def to define functions
def add(a, b):
    result = a + b
    print(f'The result is {result}')

def subtract(a, b):
    result = a -b
    print(f'The result is {result}')

def multiply(a, b):
    result = a * b
    print(f'The result is {result}')

def divide(a, b):
    result = a / b
    print(f'The result is {result}')

# user prompt 
prompt = input("What type of calculation would you like to do? (add | subtract | mult | div)")
# inputs for the numbers
num1 = int(input('What is the 1st number?: '))
num2 = int(input('What is the 2nd number?: '))
# if/elif (else if) for each prompt
if prompt == "add":
    result = add(num1, num2)
elif prompt == "subtract":
    result = subtract(num1,num2)
elif prompt == "multiply":
    result = multiply(num1,num2)
elif prompt == "divide":
    result = divide(num1,num2)
else: 
    result = None
    print("What have you done? You blew up the server")

