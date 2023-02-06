# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

is_running = True
print('Welcome to calculator!')

while is_running:
    calc = input('What kind of calculation would you like to do? (add, subtract, multiply, divide)\n> ')

    first_num = float(input(f'Okay great, so you want to {calc} some numbers. What\'s the first number?\n> '))

    second_num = float(input(f'Gotcha, {first_num}. What\'s the second number?\n> '))

    if calc == "add":
        add_result = (first_num + second_num)
        print(f'So turns out {first_num} plus {second_num} is {add_result}.')
    elif calc == "subtract":
        sub_result = (first_num - second_num)
        print(f'Okay I did some computing and {first_num} minus {second_num} is {sub_result}.')
    elif calc == "multiply":
        mult_result = (first_num * second_num)
        print(f'If you multiply {first_num} by {second_num} you get {mult_result}.')
    elif calc == "divide":
        div_result = (first_num / second_num)
        print(f'When you divide {first_num} by {second_num} you get {div_result}.')
    else:
        print("Hmm, didn't catch that. Maybe check your spelling?")

    quit = input('Want to calculate something else? (yes/no)\n> ')
    if quit == 'no':
        print('See ya 👋🏼')
        is_running = False

