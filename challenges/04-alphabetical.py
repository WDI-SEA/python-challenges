# # You'll need to use a couple of built in functions to alphabetize a string. 
# # Try to avoid looking up the exact answer and look at built in functions for
# # lists and strings instead.
# def alphabetize_string(string):
#     # convert string to a list of characters
#     chars = list(string)
#     # sort the list in alphabetical order
#     chars.sort()
#     # join the list of characters back into a string
#     alphabetized_string = ''.join(chars)
#     return alphabetized_string

# # example usage
# user_string = input("Give me a string to alphabetize\n")
# result = alphabetize_string(user_string)
# print("Alphabetized:", result)



# print('Please Enter Anything  to Reverse.')
# 00
# string = input()
# sorted_string = sorted(string)
# new_string = "".join(sorted_string)
# print(new_string)



def reverse_str():
    # Ask the user to enter a string
    string = input("Enter a something: ")
#   slicing method
    reversed_str = string[::-1]
    return reversed_str

# Example usage:
print(reverse_str())




