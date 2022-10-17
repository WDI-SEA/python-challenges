# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

#MY METHOD

# method = input('What calculation would you like to do? (add, sub, mult, div)?')
# x = input('What is number 1?')
# y = input('What is number 2?')

# if (method == 'add'):
#     print(int(x)+int(y))
# elif (method == 'sub'):
#     print(int(x)-int(y))
# elif (method == 'mult'):
#     print(int(x)*int(y))
# else:
#     print(int(x)/int(y))


# ## # ## # ##
#DELIVERABLE REVIEW

#PRINT a prompt for the user
prompt = '> '
print('Enter a type of math: add, sub, mult, div')
math = input(prompt)

# GET the input from the user and store the math they would like to do and store two numbers
print('Enter the first number')
num_one = int(input(prompt))
print('Enter the second number')
num_two = int(input(prompt))
print(f"input user data: math{math}, num1:{num_one}, num2: {num_two}")


#based on the math, do math with the two input numbers
operations = {
    "add": num_one + num_two,
    "sub": num_one - num_two,
    "mult": num_one * num_two,
    "div": num_one / num_two,
}

if math in operations:
    print(f'result {operations[math]}')
else:
    print(f'{math} is not a valid math.')