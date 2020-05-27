# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
def sorterd(word):
    results = sorted(word)
    sepa = ','
    resultss = sepa.join(results)
    print(resultss)


sorterd('yellow')