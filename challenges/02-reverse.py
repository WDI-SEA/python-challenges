# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

# STRING REVERSE
string_one = [5, 4, 3, 2, 1]
string_one.reverse()
print(string_one)

# ITERATE THROUGH LOOP-
string_two = [10,20,30,40]
for element in reversed([10,20, 30] ): print(element)

# REVERSE LINE
# string_three ="killer bunny"
# print(string_three[::-1])

# # USING SLICING
# string_four = "coconuts"
# print(string_four[::-1])

user_string =input("enter a string ")
for letter in reversed(user_string): print(letter)


# ================== review answers ====================
#  while loop
should_run = True

while should_run:
    print("hello give me a string. enter q to quit")
    string = input (">")

    new_string=""

    if string == "q":
        should_run = False


    for char in string:
        new_string = char + new_string

    print(new_string)

# while loo