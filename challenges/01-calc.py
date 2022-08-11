# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


calculator = input("what calculation would you like to do(add, sub, mult, dev)")

first_val = input("what is number one")

second_val = input("what is number two")

if calculator == "add":
    print(f"The sum is {int(first_val) + int(second_val)}")
elif calculator == "sub":
    print(f"The sum is {int(first_val) - int(second_val)}")
elif calculator == "mult":
    print(f"The sum is {int(first_val) * int(second_val)}")
elif calculator == "div":
    print(f"The sum is {int(first_val) / int(second_val)}")





