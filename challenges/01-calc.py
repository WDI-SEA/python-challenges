# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
def calc():
    calculation = input('What calculation would you like to do? (add, sub, mult, div)')
    print(calculation)
    x = input('What is number 1?')
    print(x)
    y = input('What is number 2?')

    methods = {
        "add": int(x) + int(y),
        "mult": int(x) * int(y),
        "div": int(x) / int(y),
        "sub": int(x) - int(y)
        }

    if (calculation in methods):
        return methods[calculation]
    else:
        return(print("that's not good math. Try again!"))
# print(y)
# if (calculation == "add"):
#     result = int(x) + int(y)
# elif(calculation == "sub"):
#     result = int(x) - int(y)
# elif(calculation == "mult"):
#     result = int(x) * int(y)
# elif(calculation == "div"):
#     result = int(x) / int(y)
# else:
#     print("Don't have correct input for calculation")
print(calc())
 
    
    