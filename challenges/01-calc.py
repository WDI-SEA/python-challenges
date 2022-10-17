# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calculator():
    # get all user input
    method = input("what method would youlike to use?\n")

    # get number from user
    x = int(input("what is number 1?\n"))
    y = int(input("what is number 2?\n"))

    methods = {
        "add": x + y,
        "multiply": x * y,
        "div": x / y,
        "sub": x - y,
    }

    if (method in methods):
        return methods[method]
    else:
        return print ("Argh - you did not give a correct metho! Try again.")

print(calculator())

# print a prompt for the user
# prompt = "> "

# print("Enter a type of math: add, sub, mult, div")
# math = input(prompt)
# print(f"given math {math}")

# # get input from the user and store the math they would like to do and staore 2 numbers
# print("enter the 1st number")
# num_one = int(input(prompt))
# print("enter the 2nd number")
# num_two = int(input(prompt))

# print(f"input user data: math {math}, num 1: {num_one}, num 2: {num_two}")

# # base on the math, do the math with the 2 input numbers
# operations = {
#     "add": num_one + num_two,
#     "sub": num_one - num_two,
#     "div": num_one / num_two,
#     "mult": num_one * num_two
# }

# if math in operations: 
#     print(f"result{operations(math)}")
# else:
#     print(f'{math} is not valid math')
# # get input from the user and store their input in 2 variables

# display the result to the user