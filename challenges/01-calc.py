# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


def calc(num1,num2,op):
    num1=int(num1)
    num2=int(num2)
    if (op=="add"):
        return num1+num2
    elif (op=="multiply"):
        return num1*num2
    elif (op=="subtract"):
        return num1-num2
    elif (op=="divide"):
        return num1/num2
    else:
        return "Invalid operation."


op = input("What operator would you like to use? Type add, multiply, subtract, or divide")
n1 = input("First number = ")
n2 = input("Second number = ")

print("Your result is ", calc(n1,n2,op))