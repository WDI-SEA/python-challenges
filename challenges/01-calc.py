# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


def calculator():
    operator = input('What calculation would you like to do? (add, sub, mult, div)\n')
    first_number = int(input('What is number 1?\n'))
    second_number = int(input('What is number 2?\n'))
    def math(operator):
        match operator:
            case 'add':
                return first_number + second_number
            case 'sub':
                return first_number - second_number
            case 'mult':
                return first_number * second_number
            case 'div':
                return first_number / second_number
    print(f'Your result is {math(operator)}')

        
    
calculator()
