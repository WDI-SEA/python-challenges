# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

user_string = input("Give me a string to alphabetize\n")
chars = []

for char in user_string:
  chars.append(char)

chars.sort()
sorted_string = ""

for char in chars:
  sorted_string += char
print(sorted_string)
# print(chars.sort())
