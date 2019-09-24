# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

user_string = input("Give me a string\n")
string_length = len(user_string)
slicedString=user_string[string_length::-1]
print(slicedString)


# Bryan's answer
# for letter in user_string:
#    str_list = []

# str_list.sort()
# print("".join(map(str, str_list)))

