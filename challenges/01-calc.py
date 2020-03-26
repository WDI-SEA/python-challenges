# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def get_user_input():
  return input("Enter a number: ")

def calculator():
  calc_type = input("What calculation would you lie to do? (add, sub, mult, div\n")
  valid_type = False
  while(valid_type == False):
    if (calc_type == "add"):
      valid_type = True
      num = input("What is number 1?")
      num_2 = input("What is number 2?")
      print(str(int(num) + int(num_2)))
    elif (calc_type == "sub"):
      valid_type = True
      num = input("What is number 1?")
      num_2 = input("What is number 2?")
      print(str(int(num) - int(num_2)))
    elif (calc_type == "mult"):
      valid_type = True
      num = input("What is number 1?")
      num_2 = input("What is number 2?")
      print(str(int(num) * int(num_2)))
    elif (calc_type == "div"):
      valid_type = True
      num = input("What is number 1?")
      num_2 = input("What is number 2?")
      print(str(int(num) / int(num_2)))
    else:
      print("Not a valid calculation type. Try again (add, sub, mult, div")

calculator()