# Calc
operator = input('What action would you like to perform? ')
num1 = int(input('What is the first number? '))
num2 = int(input('What is the second number? '))
result = 'Bad operator?'

if operator == 'add':
    result = num1 + num2
elif operator == 'sub':
    result = num1 - num2
elif operator == 'div':
    result = num1 / num2
elif operator == 'mult':
    result = num1 * num2

print(f'Your result was {result}!')