# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def sort_string(s):
    s = list(s)
    s.sort()
    return "".join(s)

input_string = input("Enter a string: ")
sorted_string = sort_string(input_string)
print("Sorted string:", sorted_string)
