# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

### Challenge 1 - Calculator

# print a promptfor the user
prompt = "> "
print("Enter a type of math: addition, subtraction, multiplication, division")
math = input(prompt)
print(f"given math {math}")
# get input from the user and store the math they would like to do and store two numbers
print("Enter the first number")
num_one = input(prompt)
print("Enter the second number")
num_two = input(prompt)

print(f"input user data: math {math}, num 1 {num_one}, num 2 {num_two}")
# based on the math, do math with the two input numbers
operations = {
    "addition": num_one + num_two,
    "subtraction": num_one - num_two,
    "multiplication": num_one * num_two,
    "division": num_one / num_two
}

if math in operations:
    print(f"result {operations[math]}")
else:
    print(f"{math} is not a valid math")
# display the result to the user

