# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calculator():
    print('Input what action you wish to perform on the two input feilds options are as follows:\n (add, subtract, multiply, divide)')
    math = input('insert your choice here:')
    math = math.strip()

    number_one = input('Input a number here')
    try:
        number_one = float(number_one)
    except ValueError:
        print('I said number you fooligan')
        calculator()
    number_two = input('Input a second number here')
    try:
        number_two = float(number_two)
    except ValueError:
        print('Seriously, I told you to input a number, come on.')
        calculator()
    
    switch = {
        'add' : number_one + number_two,
        'subtract' : number_one - number_two,
        'multiply' : number_one * number_two,
        'divide' : number_one / number_two
    }
    result = switch.get(math)

    if result is not None:
        print('here is your output: {result}\n')
    else:
        print('Bruh, I told you your operator options. Stop being extra and retry already.')
        calculator()
calculator()