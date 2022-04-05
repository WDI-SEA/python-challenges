# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabetical(str):
    strList = list(str)
    strList.sort()
    print("".join(strList))
