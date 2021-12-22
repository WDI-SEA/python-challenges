# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

user_input = input("Insert letters to be sorted alphabetically: ")

user_sort = sorted(user_input)
user_sort=''.join(user_sort)

print(user_sort)