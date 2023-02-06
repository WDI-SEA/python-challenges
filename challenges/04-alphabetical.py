# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

# def alphabetize_string(string):
#     return sorted(string)

# print(alphabetize_string("hello"))

string = input("Enter a string to alphabetize: ")

if string == "":
    print("Please enter a string")
else:
    print("Alphabetized: ", (sorted(string)))




