# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calc(num1,num2,t):
    num1=int(num1)
    num2=int(num2)
    if (t=="add"):
        return num1+num2
    elif (t=="mult"):
        return num1*num2
    elif (t=="sub"):
        return num1-num2
    elif (t=="div"):
        return num1/num2
    else:
        return "Invalid operation."


t = input("What calc would you like to do? (add,sub,mult,div)")
n1 = input("What is your number 1?")
n2 = input("What is your number 2?")

print("You result is ", calc(n1,n2,t))
