# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

text = input("Enter a string to alphabetize:\n ")

print('text:', text)
# split string into a list
char_list = [char for char in text]
# sort list
char_list.sort()
# join list into a string
output = ''.join(char_list)

print("output:", output)

