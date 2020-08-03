# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# add function
def add(x,y):
    return x+y

# sub function 
def sub(x ,y):
    return x-y

# mult function
def mult(x,y):
    return x*y

# div function
def div(x,y):
    return x/y

#main function 
print("What calulation would you like to do?\n")
print ("add | sub | mult | div")

while True:
    choice = input("Enter your choice: ")
    # check the choice 
    if choice in ("add", "sub", "mult", "div"):
        num1 = int(input("What is your number 1?"))
        num2 = int(input("What is your number 2?"))

        if choice == "add":
            print("Your result is ", add(num1,num2))
        elif choice == "sub":
            print("Your result is ", sub(num1,num2))
        elif  choice == "mult":
            print("Your result is ", mult(num1,num2))
        elif choice == "div":
            print("Your result is ", div(num1,num2))
        break 
    else:
        print("Invalid Input") 
