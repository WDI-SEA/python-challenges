# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


my_str = "hello"

# print(dir(list))

# my_li = ['h', 'e', 'l', 'l', 'o']
# my_li.sort()
# print(my_li)

def sort_string(string):
    # # convert string to list
    # temp_li = list(string)
    # # sort list
    # temp_li.sort()
    # convert list to string
    temp_li = sorted(string)
    return ''.join(temp_li)

print(sort_string(my_str))
print(type(sorted("hello")))