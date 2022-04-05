# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

prompt1 = input('What is your string?')

# convert string into a list
new_list = list(prompt1)

# sort the list
new_list.sort()

join_str = ''.join(new_list)

print(join_str)