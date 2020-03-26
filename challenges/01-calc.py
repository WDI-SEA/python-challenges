# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


#print("What calculation would you like to do? (add, sub, mult, div)")
#if statement, like if "add" elif "sub" elif "mult" elif "div" else nothing
#print("what is number 1?") input(prompt)
#set variable to answer a = int(input())
#pring("What is number 2?")
#complete calculation
#print(f"your result is {result}"")

def calculator():
  operator = input("What calculation would you like to do? (add, sub, mult, div) \n")

  a = int(input("What is your first number? \n"))
  b = int(input("What is your second number? \n"))
  print("Calculating...")

  if (operator == "add"):
    result = a + b
    print(result)
  elif (operator == "sub"):
    result = a - b
    print(result)
  elif (operator == "mult"):
    result = a * b
    print(result)
  elif (operator == "div"):
    result = a/b
    print(result)
  else: 
    print("Hmm something went wrong...")

calculator()

