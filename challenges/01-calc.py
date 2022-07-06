# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calc(): 
    print('Would you like to add, subtract, multiply or divide')
    method = input()
    print('whats the first number?')
    num1 = input()
    print('whats the second number?')
    num2 = input()
  
    if(method == 'add'):
        total = float(num1) + float(num2)
        return total
    elif(method == 'subtract'):
        total = float(num1) - float(num2)
        return total
    elif(method == 'multiply'):
        total = float(num1) * float(num2)
        return total
    elif(method == 'divide'):
        total = float(num1) / float(num2)
        return total
    else:
        print('that is not a method')


print(calc())