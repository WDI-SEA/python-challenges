# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

request = input('What operation do you want to use? (add, sub, mult, div) ')
firstNum = float(input('What is the first number? '))
secondNum = float(input('What is the second number? '))
if (request == 'add'):
    print(firstNum + secondNum)
elif (request == 'sub'):
    print(firstNum - secondNum)
elif (request == 'mult'):
    print(firstNum * secondNum)
elif (request == 'div'):
    print(firstNum / secondNum)
else:
    print('That was not a valid operation')
