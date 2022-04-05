# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
 

operator = input("What would you like to do? (add, sub, multiply ,divide)")

num1 = input("What is the first number?")
num2 = input("What is the second number?")

if operator == "add" :
    result = int(num1) + int(num2)
    print(f"The sum is {result} ")
elif operator == "subtract" :
    result = int(num1) - int(num2)
    print(f"the difference is {result}")
elif operator == "multiply" :
    result = int(num1) * int(num2)
    print(f"the product is {result}")
elif operator == "divide" :
    result = int(num1) / int(num2)
    print(f"the quotient is {result}")
else :
    print("Invalid operator")


