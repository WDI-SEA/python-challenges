# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

s = "lkjfsldkfjssjhfebglskfjgsaglsdgjfsaoinvfskafd"

# convert to list
li = list(s)

# list .sort
li.sort()
# convert to a string
text = "".join(li)
# print it out
print(text)