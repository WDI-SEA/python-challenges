# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# ````````
# Create a simple calculator that first asks the user what method they would like
# to use (addition, subtraction, multiplication, division) and then asks the user
# for two numbers, returning the result of the method with the two numbers. Here
# is a sample prompt:

# ```
# What calculation would you like to do? (add, sub, mult, div)
# add
# What is number 1?
# 3
# What is number 2?
# 6
# Your result is 9
# ```
# SOLUTION
prompt = '>'
print('enter a type of math: add, sub, multi, div')

math = input(prompt)
print(f'given math {math}')
# get the input from the user and store the math they would like to do plus two numbers
print('Enter the first number')
num_one = int(input(prompt))
print('Enter he second number')
num_two = int(input(prompt))

print(f'input user data: math {math}. num 1 {num_one}, num 2 {num_two}')

# based on the math, do math with the two input numbers
operations = {
    "add": num_one + num_two,
    "sub": num_one - num_two,
    "multi": num_one * num_two,
    "div": num_one / num_two
}

if math in operations:
    print(f'result {operations[math]}')
else:
    print(f'{math} is not a valid math.')