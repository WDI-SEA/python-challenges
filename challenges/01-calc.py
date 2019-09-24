# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# name = input('Hi! What is your name?')
# age = int(input('How old are you?'))
# print(f'{name} is {age} years old!')

def fun_math():
    result = 0
    math_method = input('What kind of math would you like to do? Add, subtract, multiply, divide?')
    num1 = input("What is number 1? ")
    num2 = input("What is number 2? ")

    if math_method == 'add':
        result = int(num1) + int(num2) 
    elif math_method == 'subtract':
        result = int(num1) - int(num2)
    elif math_method == 'subtract':
        result = int(num1) - int(num2) 
    elif math_method == 'multiply':
        result = int(num1) * int(num2)
    elif math_method == 'divide':
        result = int(num1) / int(num2) 
    else:
        print(f"Sorry, that's not an eligible response")
        return
    
    print(f"Your result is {result}")
    return
    

fun_math()
