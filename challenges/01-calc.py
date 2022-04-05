# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

print("What calculation would you like to do? (add, sub, mult, div)")
calc_type = input()
print("What is the first number?")
num1 = input()
print("What is the second number?")
num2 = input()
if calc_type == "add":
    num_sum = int(num1) + int(num2)
    print(f"The sum of both numbers is: {num_sum}")

elif calc_type == "sub":
    num_sub = int(num1) - int(num2)
    print(f"The difference of both numbers is: {num_sub}")

elif calc_type == "mult":
    num_mult = int(num1) * int(num2)
    print(f"The product of both numbers is: {num_mult}")

else:
    num_div = int(num1) / int(num2)
    print(f"The dividend of both numbers is: {num_div}")

