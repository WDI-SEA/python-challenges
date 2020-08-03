# user prompt
operator = input("What calculation would you like to do: add, sub, mult, div? ")

# first number prompt
first = int(input("whats the first number that will be used for this calculation? "))

# second number prompt
second = int(input("whats the first number that will be used for this calculation? "))

# conditional to execute correct calculation
if operator == "add":
    print("{}+{}= ".format(first, second))
    print(first+second)
elif operator == "sub":
    print("{}-{}= ".format(first, second))
    print(first-second)
elif operator == "mult":
    print("{}*{}=".format(first, second))
    print(first*second)
elif operator == "div":
    print("{}/{}=".format(first, second))
    print(first/second)
else:
    print("there was an error calculating!")