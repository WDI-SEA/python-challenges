# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alpha_sort(input_string):
    input_list = list(input_string)
    input_list.sort()
    return "".join(input_list)

print(alpha_sort("banana"))