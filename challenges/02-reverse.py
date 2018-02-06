def reverse(s):
    str = ""
    for i in s:
        str = i + str
        return str
s = reverse_me

print('original is': ",end="")
print(s)

print("the reversed string(using loops) is:",end="")
print(reverse(s))

