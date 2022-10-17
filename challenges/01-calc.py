# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

from ast import operator
from importlib.resources import open_binary


# num_one = int(input("enter first number"))
# num_two = int(input("enter second number"))
# operator = input("choose your operator")

def calculate():
    if operator == "+":
        print (num_one + num_two )
    elif operator == "-":
        print (num_one - num_two)
    elif operator == "*" or operator =="x":
        print (num_one * num_two)
    elif operator == "/":
        print (num_one / num_two)

# calculate()

# ========================review answers=====================================
# print user prompt
prompt = ">"
print("Enter function: add, sub, mult, div")
math = input(prompt)
print(f"given math {math}")

# get input and store the math they would like to do and store #s
print("Enter first num")
num_one = int(input(prompt))
print("Enter your second num")
num_two = int(input(prompt))

print(f"input user data: math {math}, num 1 {num_one}, num 2 {num_two}")


# perform math equation based on user input
# using a dictionary
operations ={
    "add": num_one + num_two,
    "sub": num_one - num_two,
    "mult": num_one * num_two,
    "div": num_one / num_two,
}

if math in operations:
    print(f"result {operations[math]}")
else:
    print(f"{math} is not a valid math")
# display result

