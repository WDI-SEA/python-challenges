# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

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

# print a prompt for the user
prompt = '> '
print("Enter a type of math: add, sub, mult, div")
math = input(prompt)

# get the input from the user and store the math they would like to do and store two numbers
print("Enter the first number")
num_one = int(input(prompt))
print("Enter the second number")
num_two = int(input(prompt))

# print(f"input user data: math {math}, num 1 {num_one}, num 2 {num_two}")

# based on the math, do math with the two input numbers
operations = {
    "add": num_one + num_two,
    "sub": num_one - num_two,
    "mult": num_one * num_two,
    "div": num_one / num_two
}

# display the result to the user
if math in operations:
    print(f'result {operations[math]}')
else:
    print(f'{math} is not a valid math.')
    