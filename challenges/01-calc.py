# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# good_morningMsg = input("Enter a good morning message")
# good_morningXs = input("How many times would you like to hear good morning? :")
# for i in range (int(good_morningXs)):
#     print(good_morningMsg)

# Keep program running

operator = input("Choose an operator: +  -  *  /")
num1 = int(input("What's number 1?"))
num2 = int(input("What's number 2?"))

# if operator == '+':
#     add = num1 + num2
#     print("Your total is ", add)
# if operator == '-':
#     sub = num1 - num2
#     print("Your total is ", sub)
# if operator == '*':
#     result = num1 * num2
#     print("Your total is ", result)
# if operator == '/':
#     result = num1 / num2
#     print("Your total is ", result)

###Class review
#match case
match operator:
    case "+":
        add = num1 + num2
        print(f"Your total is {add}" )
    case "-": 
        sub = num1 - num2
        print(f"Your total is {sub}")
    case "*":
        result = num1 * num2
        print(f"Your total is {result}")
    case "/":
        result = num1 / num2
        print(f"Your total is {result}")