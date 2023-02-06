# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calculator():
    print('What would you like to do? choose (add/sub/mult/div)')
    operation = input()

    def addition():
        print( f'What is the first number you want to {operation}?')
        firstnumber = input()
        try:
            firstnumber = int(firstnumber)
            # print(type(firstnumber))
        except:
            print('please type an integer')
            exit()

        print( f'What is the second number you want to {operation}?')
        secondnumber = input()
        try:
            secondnumber = int(secondnumber)
            # print(type(firstnumber))
        except:
            print('please type an integer')
            exit()
        # print(type(firstnumber))
        # print(type(secondnumber))
        result = firstnumber + secondnumber
        print( f'{result} is your result')

    def subtraction():
        print( f'What is the first number you want to {operation}?')
        firstnumber = input()
        try:
            firstnumber = int(firstnumber)
            # print(type(firstnumber))
        except:
            print('please type an integer')
            exit()

        print( f'What is the second number you want to {operation}?')
        secondnumber = input()
        try:
            secondnumber = int(secondnumber)
            # print(type(firstnumber))
        except:
            print('please type an integer')
            exit()
        # print(type(firstnumber))
        # print(type(secondnumber))
        result = firstnumber - secondnumber
        print( f'{result} is your result')

    def multiplication():
        print( f'What is the first number you want to {operation}?')
        firstnumber = input()
        try:
            firstnumber = int(firstnumber)
            # print(type(firstnumber))
        except:
            print('please type an integer')
            exit()

        print( f'What is the second number you want to {operation}?')
        secondnumber = input()
        try:
            secondnumber = int(secondnumber)
            # print(type(firstnumber))
        except:
            print('please type an integer')
            exit()
        # print(type(firstnumber))
        # print(type(secondnumber))
        result = firstnumber * secondnumber
        print( f'{result} is your result')

    def division():
        print( f'What is the first number you want to {operation}?')
        firstnumber = input()
        try:
            firstnumber = int(firstnumber)
            # print(type(firstnumber))
        except:
            print('please type an integer')
            exit()

        print( f'What is the second number you want to {operation}?')
        secondnumber = input()
        try:
            secondnumber = int(secondnumber)
            # print(type(firstnumber))
        except:
            print('please type an integer')
            exit()
        # print(type(firstnumber))
        # print(type(secondnumber))
        result = firstnumber / secondnumber
        print( f'{result} is your result')

    if operation == 'add':
        addition()
    elif operation == 'sub':
        subtraction()
    elif operation == 'mult':
        multiplication()
    elif operation == 'div':
        division()
    else:
        print('incorrect input')


calculator()

# print(type(7))