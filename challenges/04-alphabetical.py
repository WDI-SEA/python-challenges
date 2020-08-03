# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def string_reverser():
  print('Enter a string and behold as the mighty pyhton reverses it!')
  string = input('type your string here, human:')
  string = list(string)
  string = sorted(string)
  ordered_string = ''
  for letter in string:
    ordered_string += letter
    print(ordered_string)

  print('Stand in Awe of the mighty python!')

string_reverser()