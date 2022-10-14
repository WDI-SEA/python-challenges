# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


print('what you want you got choices add , sub , mult , or div')
q1 = input()
print('whats the first num')
q2 = input()
print('and the second num?')
q3 = input()

if q1 == "add":
    print('heres your answer')
    print(int(q2) + int(q3))
elif q1 == "sub":
    print('heres your answer')
    print(int(q2) - int(q3))
elif q1 == 'mult': 
    print('heres your answer')
    print(int(q2) * int(q3))
else:
    print('heres your answer')
    print(int(q2) / int(q3))
