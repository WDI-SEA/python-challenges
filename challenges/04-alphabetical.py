# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

my_string = input('Your String now? ')
my_list = list(my_string)
my_list.sort()
alpha_str = ''.join(my_list)
print(alpha_str)

