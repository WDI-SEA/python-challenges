# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

alphabet = "zyxwvutsrqonmlkjihgfedcba"
arr_alphabet = list(alphabet)
arr_alphabet.sort()
print("".join(arr_alphabet))

def solution(string):
    # sorted_string = "".join(sorted(string, key=str.lower))
    # return sorted
    li = list(string)
    li.sort()
    return "".join(li)
print(solution("cba"))
print(solution("zxy"))