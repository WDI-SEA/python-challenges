# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
def calculate():
    print('Would you like to add, sub, mult, or div')
    x = input()
    print('first num')
    onest = input()
    print('second num ')
    twost = input()
    if x == 'add':
        print(int(onest) + int(twost))
    elif x == 'sub':
        print(int(onest) - int(twost))
    elif x == 'mult':
        print(int(onest) * int(twost))
    elif x == 'div':
        print(int(onest) / int(twost))
    else: 
        print('wrong')

# calculate()

# if/else if/else
# og python dictionary switch case
# match case (newest way)
prompt = '> '
print('what math')
math_type = input(prompt)
print('Enter the first num')
num_one = input(prompt)
print('second')
num_two = input(prompt)

num_one = int(num_one)
num_two = int(num_two)

match math_type:
    case 'add':
        print(num_one + num_two)
    case _:
        print('weewooweewooweewoo')