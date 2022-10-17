# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

prompt = '> '
print("Add, Subtract, Multiply, Divide")
math = input(prompt)

print("Number one: ")
num_one = int(input(prompt))
print("Number two:")
num_two = int(input(prompt))
print(f"input: math {math}, number one {num_one}, number two {num_two}")

operations = {
    "add": num_one + num_two,
    "subtract": num_one - num_two,
    "multiply": num_one * num_two,
    "divide": num_one / num_two
}

if math in operations:
    print(f"result {operations[math]}")
