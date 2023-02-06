# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
my_str = "helo"
def sort_string(string):
    temp_li = list(string)
    temp_li.sort()
    return "".join(temp_li)
print(sort_string(my_str))