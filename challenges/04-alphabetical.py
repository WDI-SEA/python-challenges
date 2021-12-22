# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabetical_order(str):
    split_apart = sorted(str)
    print(''.join(split_apart))

alphabetical_order('mackenzie')