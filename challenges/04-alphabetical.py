# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


def alphabetize_string(string):
    return ''.join(sorted(string))

string = "hello"
alphabetized_string = alphabetize_string(string)
print(alphabetized_string)

#  The sorted() function returns a sorted list of the given iterable. The sorted() function doesn't modify the original list. The join() method is a string method and returns a string in which the elements of sequence have been joined by str separator.