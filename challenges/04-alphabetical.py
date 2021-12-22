# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

# ===BUILT IN SORT BY BUILT IN SORT BY ASCII VALUE=== #


string = "hello"
string = list(string)

def ordSortSimple(str):
    print(ord(str))
    return ord(str)

string.sort(key=ordSortSimple)
"".join(string)

print(string)


# ===INSERTION SORT BY CONVERSION TO ASCII AND BACK === #

# REGULAR STRING
stringv1 = "stringarray"
# ASCII VALUE ARRAY
mutated_string = []
# CONVERSION BACK ARRAY
new_string = []

def ord_sort(string):

    # NORMALIZE VALUE TO UPPER
    string = string.upper()
    # STRING SPLIT INTO LIST
    string = list(string)

    # convert string array into num array:
    for letter in string:
        mutated_string.append(ord(letter))
    
    print(mutated_string)

    # INSERTION SORT ALGORITHIM
    for index in range(1, len(mutated_string)):
        curVal = mutated_string[index]
        position = index - 1

        while position >= 0 and mutated_string[position] > curVal:
            mutated_string[position + 1] = mutated_string[position]
            position -= 1
            print(mutated_string)

        mutated_string[position + 1] = curVal 

ord_sort(stringv1)

# CONVERT BACK TO CHAR VALUE
for number in mutated_string:
    new_string.append(chr(number))
    print(new_string)

# JOIN
newstringjoin = "".join(new_string)

print(f" this is mutated string :{mutated_string}")
print(f" this is new_string: {newstringjoin}")
