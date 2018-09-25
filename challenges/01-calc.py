# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def add(x, y):
  return x + y

def sub(x, y): 
  return x - y

def mult(x, y):
  return x * y 

def div(x, y):
  return x / y

method = input('What calculation would you like to do? (add, sub, mult, div)')

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if method == 'add':
   print(x,"+",y,"=", add(x,y))

elif method == 'sub':
   print(x,"-",y,"=", sub(x,y))

elif method == 'mult':
   print(x,"*",y,"=", mult(x,y))

elif method == 'div':
   print(x,"/",y,"=", div(x,y))
else:
   print("Invalid input")g