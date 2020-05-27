# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

num = input('what is your number?')
num2 = input("what is your 2nd number?")
operator = input("what is your operator?")

num = int(num)
num2 = int(num2)    
if(operator):
    if operator == "+":
        print(int(num) + int(num2))
    elif operator == "-":
        print(num - num2)
    elif operator == "/":
        print(num / num2)
    elif operator == "*":
        print(num * num2)
    else:
        print('wrong operator type')