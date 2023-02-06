# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def sort_string(str):
    return ''.join(sorted(str))
str = 'This string will turn alphabetical'
print(sort_string(str))

def sort_string(string):
    temp_li = list(string)
    temp_li.sort()
    return ''.join(temp_li)



 
# def sortString(str):
#     return reduce(lambda a, b : a + b, sorted(str))
     
# str = 'This will turn alphabetical'
# print(sortString(str))
