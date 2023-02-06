# You'll need to use a couple of built in functions to alphabetize a string.
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

string = input("what would you like to alphabetize today?: ")
alphabetized_string = "".join(sorted(string))
print(f'Here is your alphabetized string:  {alphabetized_string}')
