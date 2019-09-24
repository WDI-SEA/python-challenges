# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

equation = int(input("Enter your equation by its listed number: "))
if(equation>=1 and equation <=4):
    print("Enter two numbers: ")
    x = int(input())
    y = int(input())
    if equation == 1:
        res = x + y
        print("Result = ", res)
    elif equation == 2:
        res = x - y
        print("Result = ", res)
    elif equation == 3:
        res = x * y
        print("Result = ", res)
    else: 
        res = x / y
        print("Result = ", res)
    