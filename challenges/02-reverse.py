phrase = 'The sun will come out one day'

def string_reverse(string):
    reversed_string = ''
    for i in range(len(string)):
        reversed_string += string[len(string)-i-1]
    print(reversed_string)

string_reverse(phrase)