# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

alphabet = "abcdefghijklmnopqrstuvwxyz"
str = "supercalifragilisticexpialidocious"

def alpha(strang):
    newVal = ""
    for i in range(len(alphabet)):
        if alphabet[i] in strang:
            for j in range(len(strang)):
                if alphabet[i] == str[j]:
                    newVal = newVal + str[j]
    return newVal

print(alpha(str))