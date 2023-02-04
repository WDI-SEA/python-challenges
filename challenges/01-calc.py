# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calculator():
    first_num = 0
    second_num = 0
    
    print('What calculation would you like to do? (add, sub, mult, div)')
    calc_type = input()
    
    def add_num(first_num, second_num):
        results = int(first_num) + int(second_num)
        return str(results)
    
    def sub_num(first_num, second_num):
        results = int(first_num) - int(second_num)
        return str(results)

    def mult_num(first_num, second_num):
        results = int(first_num) * int(second_num)
        return str(results)

    def div_num(first_num, second_num):
        results = int(first_num) / int(second_num)
        return str(results)

    
    if calc_type in ('add', 'sub', 'mult', 'div'):
        print(f'What is the first number you\'d like to {calc_type}?')
        first_num = input()
        print(f'What is the second number you\'d like to {calc_type}?')
        second_num = input()
    else:
        print(f'Incorrect entry.')

    if calc_type == 'add':
        print(f'Your result is {add_num(first_num, second_num)}')
    elif calc_type == 'sub':
        print(f'Your result is {sub_num(first_num, second_num)}')
    elif calc_type == 'mult':
        print(f'Your result is {mult_num(first_num, second_num)}')
    elif calc_type == 'div':
        print(f'Your result is {div_num(first_num, second_num)}')
    
calculator()
