# Use the `input()` function to prompt a user to enter something.
birthYear = input('Enter your birth year')
# input() always returns a string value. If you ever want someone
age = 2023 - int(birthYear)
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
print(age)
