# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

string = "Hello"

# print(dir(list))

my_list = ['h', 'e', 'l', 'l', "o"]
my_list.sort()
print(my_list)

def sort_string(string): 
    temp_list = list(string)

    temp_list.sort()

    return ''.join(temp_list)

print(sort_string(string))