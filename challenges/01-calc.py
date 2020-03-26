# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

print("What calculation would you like to do? (add, sub, mult, div)")
calculation = input()
print("What is number 1?")
num_one = int(input())
print("What is number 2?")
num_two = int(input())
# Calculate result
if calculation == "sub":
  result = num_one - num_two
elif calculation == "add":
  result = num_one + num_two
elif calculation == "mult":
  result = num_one * num_two
elif calculation == "div":
  result = num_one / num_two
print(f"Your result is {result}")