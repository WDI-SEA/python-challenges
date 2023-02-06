# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


method = input("What calculation would you like to do? (add, sub, mult, div) ")
x = input("What is number 1?")
y = input("What is number 2? ")

sum = 0
if method == "add":
    sum = int(x) + int(y)
elif method == "sub":
    sum = int(x) - int(y)
elif method == "mult":
    sum = int(x) * int(y)
elif method == "div":
    sum = int(x) / int(y)
else:
    print("Invalid input")

print("Your result is: ", sum)



# is_running = True
# while is_running:

#         prompt = '>'
#         # print("Hello, user! What kind of math would you like to do? (add, sub, mult, div)")
#         # math_type = input(prompt)

#         # print("enter your first number")
#         # num_one = input(prompt)

#         # print("enter your second number")
#         # num_two = input(prompt)
#         # # print(f'math type: {math_type}, num one: {num_one}, num two: {num_two}')

#         # # convert the string to an integer
#         # num_one = int(num_one)
#         # num_two = int(num_two)

#         # match math_type:
#         #     case "add":
#         #         print(f'{num_one} + {num_two} = {num_one + num_two}')
#         #     case "sub":
#         #         print(f'{num_one} - {num_two} = {num_one - num_two}')
#         #     case "mult":
#         #         print(f'{num_one} * {num_two} = {num_one * num_two}')
#         #     case "div":
#         #         print(f'{num_one} / {num_two} = {num_one / num_two}')
#         #     case _:
#         #         print(f'Invalid input: {math_type}')
#     print("Would you like to do another calculation? [y/n]")
#     should_quit = input(prompt)
#     if should_quit == "n":
#         is_running = False
#         print("Goodbye!")
    