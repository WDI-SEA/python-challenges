# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operator = input('What calculation would you like to do? (add, sub, mult, div)')
questionOne = int(input('What is number 1?'))
questionTwo = int(input('What is number 2?'))


if operator == 'add':
    answer = questionOne + questionTwo
elif operator == 'sub':
    answer = questionOne - questionTwo
elif operator == 'mult':
     answer = questionOne * questionTwo
elif operator == 'div':
    answer =  questionOne / questionTwo

print(f'Your result is {answer}')