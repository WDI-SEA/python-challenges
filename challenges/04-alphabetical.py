# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

user_string = input("Give me a string to alphabetize\n")
letter_list = []
for letter in user_string:
    letter_list.append(letter)
letter_list.sort()
alpha_string = ''.join(letter_list)
print(alpha_string)