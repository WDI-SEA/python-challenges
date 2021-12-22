# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

function = input("What calculation would you like to do?(addition, subtraction, multiplication, division): ")
numOne = int(input("Enter your first number:"))
numTwo= int(input("Enter your second number: "))
if function == "addition":
    print(numOne+numTwo)
elif function == "subtraction":
    print(numOne-numTwo)
elif function == "multiplication":
    print(numOne*numTwo)
elif function == "division":
    print(numOne/numTwo)
else: 
    print('not a function!')
