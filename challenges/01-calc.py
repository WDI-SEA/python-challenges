# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

print("Math time")
operation = input("What would you like to do? (add, sub, mult, div) ")
num_one = input("First number? ")
num_two = input("Second number? ")
if operation == "add":
    result = int(num_one) + int(num_two)
    print(f"The result is {result}")
elif operation == "sub":
    result = int(num_one) - int(num_two)
    print(f"The result is {result}")
elif operation == "mult":
    result = int(num_one) * int(num_two)
    print(f"The result is {result}")
elif operation == "div":
    result = int(num_one) / int(num_two)
    print(f"The result is {result}")
else:
    print("invalid operation. please try again")