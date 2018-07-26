# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

#Reverse a string manually. Don't use s[::-1] (even though that's awesome). Create a new variable storing an empty string and add the letters from the first string one by one. The for loop should iterate over the length of the string and you should access letters individually.

#Below is some sample output.

#Enter a string:
#reverse_me
#em_esrever

operation = input('''Enter a string: ''')
print(operation[::-1])

initial_string = input("Type a sentence!")
new_array = []

for i in range(0, len(initial_string)):
	new_array.insert(0, initial_string[i])

reverse_string = ''.join(new_array)
print(reverse_string)