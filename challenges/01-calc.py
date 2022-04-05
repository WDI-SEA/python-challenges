# my solution:
# # Use the `input()` function to prompt a user to enter something.
# def calculator():
# # input() always returns a string value. If you ever want someone
#     prompt = input("what to calcualte\n")
# # to enter a number you have to use the `int()` function to convert
#     a = int(input("num 1\n"))
#     b = int(input("num 2\n"))
# # what they typed in to a string.
#     operator = {
#         "add": a + b,
#         "subtract": a - b,
#         "multiply": a * b,
#         "divide": a / b  
#     }
#     if (prompt in operator):
#         return operator[prompt]
#     else:
#         return print("promt not exist")
# print(calculator())

#solution 2:
method = input('select a method: add, subtract, divide, multiply')
num1 = int(input('input a number'))
num2 = int(input('input another number'))

if method == 'add':
  print(num1 + num2)
elif method == 'subtract':
  print(num1 - num2)
elif method == 'divide':
  print(num1 / num2)
elif method == 'multiply':
  print(num1 * num2)
else:
  print('i dont think that is a math!')