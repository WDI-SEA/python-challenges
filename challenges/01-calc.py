# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calculator():
    operator = input("What calculation would you like to do? (add,sub,mult,div)")

    x = int(input("What is the first number? : "))
    y = int(input("What is the second number? : "))

    if(operator == "add"):
        result = x + y
        print (result)
    elif (operator == "sub"):
        result = x - y
        print (result)
    elif (operator == "mult"):
        result = x * y
        print (result)
    elif (operator == "div"):
        result = x / y
        print (result)
    else:
        print("Error")

calculator()

'''
OUTPUT : 
-----------------------
ADD
What calculation would you like to do? (add,sub,mult,div)add
What is the first number? : 5
What is the second number? : 8
13

SUB
What calculation would you like to do? (add,sub,mult,div)sub
What is the first number? : 5
What is the second number? : 8
-3

MULT
What calculation would you like to do? (add,sub,mult,div)mult
What is the first number? : 5
What is the second number? : 8
40

DIV
What is the first number? : 5
What is the second number? : 8
0.625
'''