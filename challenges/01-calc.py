# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

answer = input("What would you like to do? (add,subtract,divide,multiply) ")
number1 = input("What is the first number?")
number2 = input("What is the second number?")



if answer == "add":
    print(int(number1)+int(number2))
elif answer == "subtract":
    print(int(number1)-int(number2))
elif answer == "divide":
    print(int(number1)/int(number2))
elif answer == "multiply":
    print(int(number1)*int(number2))
