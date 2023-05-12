# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabetize(str):
    # sorted_str = sorted(str)
    
    # stringified = ''.join(sorted_str)

    # return stringified

    return ''.join(sorted(str))

print(alphabetize("supercalifragilisticexpialidocious"))

# convert to list approach
string = "antidisestablishmentarianism"
string_list = list(string)
string_list.sort()
string = "".join(string_list)
print(string)

# python slice syntax
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [slice start (default 0): slice end (default end of list): step (default 1)]
my_list_copy = my_list[::] # make a copy with defaults
print(my_list[::-1])
print("racecar"[::-1])