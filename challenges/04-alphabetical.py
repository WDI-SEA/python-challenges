# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
s = 'sabfgslgabdkjgbakgbksjnbflainbldfnssdnvielwfbldfkhdifgnsdk'

#convert to lisr
li = list(s)
#sort the list and covnert to string
li.sort()
#convert to new string
new_string = "".join(li)

print(new_string)