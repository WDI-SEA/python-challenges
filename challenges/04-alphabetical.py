# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

print('Gimme a string of letters please.')
string = input()
sorted_string = sorted(string)
new_string = "".join(sorted_string)
print(new_string)