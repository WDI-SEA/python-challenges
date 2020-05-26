# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


my_string = input("alphabetize this, sucka!")
my_list = sorted(my_string)
alpha_string = ''.join(my_list)
print(alpha_string)