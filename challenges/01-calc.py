# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
### Challenge 1 - Calculator

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

input_operation = input("What calculation would you like to do? add, sub, mult, div: ")
input_first_number = int(input("What is the first number?: "))
input_second_number = int(input("What is the second number?: "))

def calculator(input_operation,input_first_number,input_second_number):
    if input_operation == "add":
        print(f"Answer: {(input_first_number + input_second_number)}")
    elif input_operation == "sub":
        print(f"Answer: {(input_first_number - input_second_number)}")
    elif input_operation == "mult":
        print(f"Answer: {(input_first_number * input_second_number)}")
    else:
        print(f"Answer: {(input_first_number / input_second_number)}")

calculator(input_operation, input_first_number, input_second_number)
