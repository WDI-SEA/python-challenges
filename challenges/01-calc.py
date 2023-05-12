# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.



is_running = True

while is_running:
    prompt = '>'
    print('hello user')
    print('tell me what kind of math you want to do')
    print('Possible choices: add, sub, mul, div')
    math_choice = input(prompt)
    print(f'math choice: {math_choice}')
    print('excellent math choice! Enter the first number: ')
    number_one = input(prompt)
    print("Now, enter a second number: ")
    number_two = input(prompt)
    print(number_one, number_two)

    try:
        number_one = int(number_one)
        number_two =  int(number_two)
    except ValueError as e:
        print('that wasnt a real number')

    switch = {
        'add': number_one + number_two,
        'sub': number_one - number_two,
        'mul': number_one * number_two,
        'div': number_one / number_two
    }

    if math_choice in switch:
        print(f'result: {switch[math_choice]}')
    else: 
        print(f'i lied, {math_choice} isnt a math I know about')

    print('would you like to continue? Y/n')
    should_quit = input(prompt)
    if should_quit == 'n':
        is_running = False