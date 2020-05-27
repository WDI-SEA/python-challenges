# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

inputstrn = input("what word would you like sorted? ")

def sorter(strn): 
    strn = sorted(strn)
    print(strn)

sorter(inputstrn)