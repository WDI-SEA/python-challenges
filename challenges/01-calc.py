# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


# print prompt for user
prompt = '> '
print('What type of math function? Add, Subtract, Multiply, Divide')
math = input(prompt)
print(f"given math {math}")


# get input from user- two numbers and one math type
print("enter the first number")
number_one = int(input(prompt))
print("Enter the second number")
number_two = int(input(prompt))

print(f"input user data: math {math}, first number: {number_one}, second number: {number_two}")


# based on math, do math with the two input numbers
operations = {
     "add": number_one + number_two,
     "subtract": number_one + number_two,
     "multiply": number_one * number_two,
     "divide": number_one / number_two
}

if math in operations:
     print(f"result: {operations[math]}")
else:
     print(f"{math} is not a valid math function")

# display result to the user