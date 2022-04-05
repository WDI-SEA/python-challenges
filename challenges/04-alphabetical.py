# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def sort_string(string):
    # print(string)
    array = list(string)
    array.sort()
    # print(array)
    string = ''.join(array)
    return string

print(sort_string('supercalifragilisticexpialidocious'))
# print(dir(list))
# print(dir(str))
