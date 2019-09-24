# You'll need to use a couple of built in functions to alphabetize a string.
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


in_string = input('string to alphabetize')
str_list = []
for letter in in_str:
    str_list.append(letter)

str_list.sort()
print(''.join(map(str, str_list)))
