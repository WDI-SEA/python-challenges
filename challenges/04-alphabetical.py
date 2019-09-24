# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

word = input("What word do you want me to fuck up? ")

def alphabetize(string):
    temp = []
    for i in range(1, len(string)+1):
        temp.append(string[-i])
    newtemp = sorted(temp)
    print("".join(newtemp))

alphabetize(word)