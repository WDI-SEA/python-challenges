# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

print("add, sub, mult, div?")
method = input()
print(method)
if method == "add" or method == "sub" or method == "mult" or method == "div":
    pass
else: 
    print("invalid input.")
    method = input()

print("num 1?")
num_one = input()
print("num 2?:")
num_two = input()
if method == "add":
    result = int(num_one) + int(num_two)
    
elif method == "sub":
    result = int(num_one) - int(num_two)
    
elif method == "mult":
    result = int(num_one) * int(num_two)
    
elif method == "div":
    result = int(num_one) / int(num_two)
print("The result is", result)