# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# prompt = input('What operation would you like to perform?(add, multiply, subtract, divide)')
# num1 = input('what is the 1st number you want to use?')
# num1 = int(num1)
# num2 = input('what is the 2nd number you want to use?')
# num2 = int(num2)

# def calculate():
#     if prompt == "add":
#         return num1 + num2
#     elif prompt == "subtract":
#         return num1 - num2
#     elif prompt == "multiply":
#         return num1 * num2
#     elif prompt == "divide":
#         return num1 / num2
# print(f"your result is {calculate()}  bitch")

# name = input("What's your name? ")
# count = input("How many times shall I greet you? ")
# count = int(count)

# for i in range(count):
#   print(f"Hello {name}!")

start = input("Anthony has a couple...literally two questions for you? type ok to continue if you dare.")
prompt = input("Do you love anthony unconditionally?")
prompt2 = input('Even if he farted in your face?')
marry = 'then marry me already'


def answer():
    if prompt == "yes" and prompt2 == "yes":
        return "Anthony is happy! Will you marry him?"
    elif prompt == "no" and prompt2 == "no":
        return "Anthony wants you to leave...now"
    elif prompt == "yes" and prompt2 == "no":
        return "well its too fucking late"
    elif prompt == "no" and prompt2 == "yes":
        return "He thinks your, your wierd. but low key he wants to know what he can do to get you to love him unconditional."
    

    
print(answer())
    