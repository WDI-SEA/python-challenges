# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

inputString = input("String to alphabetize: ")

sorted_word = "".join(sorted(inputString, key=str.lower))

print("The alphabetized letters of your input string: ", sorted_word)