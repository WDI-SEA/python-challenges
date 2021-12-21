# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

question = input(
    "What calculation would you like to do? (add, sub, mult, div)\n")
num1 = int(input("Whats is your first number? \n"))
num2 = int(input("What is Your Second Number? \n"))

if (question.lower() == 'add'):
    print("Your result is", num1 + num2)
elif (question.lower() == 'sub'):
    if (num1 > num2):
        print("Your result is", num1 - num2)
    else:
        print("Your result is", num2 - num1)
elif (question.lower() == 'mult'):
    print("Your result is", num1 * num2)
elif (question.lower() == 'div'):
    print("Your result is", num1/num2)