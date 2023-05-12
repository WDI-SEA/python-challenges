# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

# convert to list approach
# string = "supercalifragilisticexpialidocious"
# string_list = list(string)
# string_list.sort()
# string = "".join(string_list)
# print(string)

# # sorted function approach
# print("".join(sorted(string)))


# python slice syntax (works on lists or strings)
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [slice start (default 0): slice end (deflaut end of list): step (defualt 1)]
my_list_copy = my_list[::] # make a copy with defaults
print(my_list[::-1])
print("hello"[::-1])

