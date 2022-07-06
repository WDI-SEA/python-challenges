# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

cal = input('what method: ')
first_num = int(input('what is the first num?: '))
second_num = int(input('what is the second num?: '))

if cal == 'add':
    print(first_num + second_num)

if cal == 'subtract':
    print(first_num - second_num)




if cal == 'multiply':
    print(first_num * second_num)

if cal == 'divide':
    print(first_num / second_num)
