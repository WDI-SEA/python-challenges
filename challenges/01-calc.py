is_running = True
while is_running:
    # display math choices and ask user to choose one
    prompt = ">"
    print("Hello friend!")
    print('Tell me what kind of math you would like to do.')
    print('Possible choices: add, subtract, multiply, and divide.')
    math_choice = input(prompt)
    print(f"Math choice: {math_choice}")

    # ask the user to input two numbers
    print('Excellent math choice! Enter the first number to use:')
    number_one = input(prompt)
    print('Now enter a second number:')
    number_two = input(prompt)

    # convert input to integers
    try:
        number_one = int(number_one)
        number_two = int(number_two)

        # perform the selected math operation
        if math_choice == 'add':
            print(f"{number_one} + {number_two} = {number_one + number_two}")
        elif math_choice == 'subtract':
            print(f"{number_one} - {number_two} = {number_one - number_two}")
        elif math_choice == 'multiply':
            print(f"{number_one} * {number_two} = {number_one * number_two}")
        elif math_choice == 'divide':
            if number_two == 0:
                print("Error: Cannot divide by zero!")
            else:
                print(f"{number_one} / {number_two} = {number_one / number_two}")
        else:
            print(f"I'm sorry, '{math_choice}' isn't a valid math operation.")

    except ValueError:
        print('That wasn\'t a valid number!')

    # ask user if they would like to continue
    print('Would you like to continue doing more math problems? (y/n)')
    should_quit = input(prompt)
    if should_quit.lower() == 'n':
        is_running = False