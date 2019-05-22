# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operation = input("What operation do you what to do? ")

if (operation == "addition"):
    num1 = input("give me the first number ")
    num1 = int(num1)
    num2 = input("give me the second number ")
    num2 = int(num2)
    print("result is {}".format(num1 + num2))

elif (operation == "subtraction"):
    num1 = input("give me the first number ")
    num1 = int(num1)
    num2 = input("give me the second number ")
    num2 = int(num2)
    print("result is {}".format(num1 - num2))

elif (operation == "multiplication"):
    num1 = input("give me the first number ")
    num1 = int(num1)
    num2 = input("give me the second number ")
    num2 = int(num2)
    print("result is {}".format(num1 / num2))

elif (operation == "division"):
    num1 = input("give me the first number ")
    num1 = int(num1)
    num2 = input("give me the second number ")
    num2 = int(num2)
    print("result is {}".format(num1 * num2))

else:
    print("that operation does not exist!!")
