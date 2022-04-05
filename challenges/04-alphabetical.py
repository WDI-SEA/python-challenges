# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabetize(string):
  # turn the string into a list
  string_list = list(string)
  # sort the letters
  string_list.sort()
  # join letters
  string_list =''.join(string_list)
  return(string_list)

print(alphabetize('loona is the best'))