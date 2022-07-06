# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
string = input('String to be alphabetized?\n')
my_list=list(string)
my_list.sort()
ordered_string = ''.join(my_list)
print(ordered_string)