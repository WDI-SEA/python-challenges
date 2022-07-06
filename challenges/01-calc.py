# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


operations = input("What calculation would you like to do? (add, sub, mult, div)")
print(operations)
num1 = int(input("What is number 1?"))
print(num1)
num2 = int(input("What is number 2?"))
print(num2)

def calculator(operations, num1, num2):
    if(operations=="add"):
        return num1+num2
    elif(operations=="sub"):
        return num1-num2
    elif(operations=="mult"):
        return num1*num2
    elif(operations=="div"):
        return num1/num2

print(calculator(operations, num1, num2))