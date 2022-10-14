# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

word = input('enter a word ')

my_list = []
l = len(word)
for i in range (0,l):
    my_list.append(word[i])
 
 
for i in range(0,l):
    for a in range(0,l):
        if my_list[i]<my_list[a]:
            my_list[i],my_list[a]=my_list[a],my_list[i]
a = ""
 
for i in range(0,l):
    a = a+my_list[i]
 
print(a)