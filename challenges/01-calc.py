# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

process = input('What calculation would you like to do? (add, sub, mult, div) :')
process_list = ('add', 'sub', 'mult', 'div')

while not process in process_list:
    if process in process_list:
        break
    else:
        process = input('You made an inavlid selection. Please choose : add, sub, mult, div : ')

num_one = input('Please, enter a number : ')
num_two = input('Please, enter a second number :')

def add_numbers(first_num, second_num):
    sum = int(first_num) + int(second_num)
    return sum

def sub_numbers(first_num, second_num):
    difference = int(first_num) - int(second_num)
    return difference

def mult_numbers(first_num, second_num):    
    product = int(first_num) * int(second_num)
    return product

def div_numbers(first_num, second_num):
    while int(second_num) == 0:
        if int(second_num) != 0:
            break
        else:
            second_num = input('Please, enter a second number other than 0 :')
    quotient = int(first_num) / int(second_num)
    return quotient

if process == 'add':
    print('Your result is {}'.format(add_numbers(num_one, num_two)))
elif process == 'sub':
    print('Your result is {}'.format(sub_numbers(num_one, num_two)))
elif process == 'mult':
    print('Your result is {}'.format(mult_numbers(num_one, num_two)))
elif process == 'div':
    print('Your result is {}'.format(div_numbers(num_one, num_two)))