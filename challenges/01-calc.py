# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


# user = input('Add, Subtract, Multiply, or Divide')

# num1 = input('Value 1')

# num2 = input ('Value 2')

# if (user == 'add'):
#     result = int(num1) + int(num2)
# if (user == 'subtract'):
#     result = int(num1) - int(num2)
# if (user == 'multiply'):
#     result = int(num1) * int(num2)
# if (user == 'divide'):
#     result = int(num1) / int(num2)



# input(f'{result}')



# ````
# what calculation would you like to do? (add, sub, mult, div)
# add
# What is number 1?
# 3
# what is number 2?
# 6
# Your result is 9
# ```

# print a prompt for the user
prompt = '> '
print('Enter a type of math: add, sub, mult, div')
math = input (prompt)
print(f"given math {math}")
# get the input from the user and store the math they would like to do and store two numbers
print("Enter the first number")
num_one = int(input(prompt))
print("Enter the second number")
num_two = int(input(prompt))

# print(f"input user data: math {math}, num 1 {num_one}, num 2 {num_two}")
# based on the math, do math with two input numbers
operations = {
    "add": num_one + num_two,
    "sub": num_one - num_two,
    "mult": num_one * num_two,
    "div": num_one / num_two
}

if math in operations:
    print(f'result {operations[math]}')
else:
    print(f'{math} is not a valid math.')
# display the result to the user

