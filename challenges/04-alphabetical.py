# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

print("Enter a string to alphabetize")
string = input()
list = []
list[:0] = string
sort_list = sorted(list)
print(''.join(sort_list))