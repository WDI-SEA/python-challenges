# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

math = input("What calculation would you like to do? (add, sub, mult, div)")

num_one = input("What is the first number?")

num_two = input("What is the second number?")
 
def do_math(number_one, number_two):
    if "add" in math:
       return number_one + number_two
    elif "sub" in math:
        return number_one - number_two
    elif "mult" in math:
        return number_one * number_two
    elif "div" in math:
        return number_one / number_two
    
# Output
print(do_math(int(num_one), int(num_two)))