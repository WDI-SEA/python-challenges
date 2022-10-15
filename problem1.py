# Create a simple calculator that first asks the user what method they would like to use (addition, subtraction, multiplication, division) and then asks the user for two numbers, returning the result of the method with the two numbers. Here is a sample prompt:

def add(num1, num2):
  return num1 + num2

# print(add(3,4))

def subtract(num1, num2):
  return num1 - num2

# print(subtract(3,4))

def multiply(num1, num2):
  return num1 * num2

# print(multiply(3,4))

def divide(num1, num2):
  return num1 / num2

# print(divide(3,4))

operation = input("What calculation would you like to do? (add, subtract, multiply, divide) ")

user_input = str(operation)

# print(user_input)

number1 = input("What is number 1? ")

user_number1 = int(number1)

# print(user_number1)

number2 = input("What is number 2? ")

user_number2 = int(number2)

# print(user_number2)

if user_input == "add":
  print(f"Your result is {user_number1 + user_number2}")
elif user_input == "subtract":
  print(f"Your result is {user_number1 - user_number2}")
elif user_input == "multiply":
  print(f"Your result is {user_number1 * user_number2}")
elif user_input == "divide":
  print(f"Your result is {user_number1 / user_number2}")
else:
  print("Please enter a valid operator or number.")
