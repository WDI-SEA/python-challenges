# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.



# age = input("Please enter your age: ")
# age = int(age)
# print("In ten years, you will be", age + 10, "years old.")
# 


# input to allow users to enter something
calc = input("Enter the a num operation you like to do:  (add, sub, mult, div) ")

num1 = int(input("The First Number: "))
num2 = int(input("The Second Number: "))

if calc == "add":
    result = num1 + num2
elif calc == "sub":
    result = num1 - num2
elif calc == "mult":
    result = num1 * num2
elif calc == "div":
    result = num1 / num2
else:
    print("Invalid input, please try again.")
    exit()

print("Your result is", result)


