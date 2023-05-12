# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


# convert to lsit approch
string = "sjndgnsndflafdkjsngnsdffgh"
string_list = list(string)
string_list.sort()
string = "".join(string_list)
print(string)

# sorted function approach
print("".join(sorted(string)))


# python slice syntax
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [slice start (default 0): slice end(deflaut 0): step (defualt 1)]
my_list_copy = my_list[::] # make a copy with defaults 
# print(my_list[::2]) # increments by 2's
# print(my_list[::-1]) # reverses the list
