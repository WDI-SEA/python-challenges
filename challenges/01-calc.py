# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

is_running = True

while is_running:
    prompt = "> "
    print("Hello, user! What kind of math would you like to do today? (add, sub, mult, div)")
    math_type = input(prompt)

    print("Enter the first Number")
    num_one = input(prompt)

    print("Enter the second Number")
    num_two = input(prompt)
    # print(f"math type: {math_type}, num one: {num_one}, num two: {num_two}")

    # if/else if/else
    # og python dictionary switch case
    # match case

    # convert to numbers 
    num_one = int(num_one)
    num_two = int(num_two)

    match math_type:
        case "add":
            print(f"{num_one} + {num_two} = {num_one + num_two}")
        case "sub":
            print(f"{num_one} - {num_two} = {num_one - num_two}")
        case "mult":
            print(f"{num_one} * {num_two} = {num_one * num_two}")
        case "div":
            print(f"{num_one} / {num_two} = {num_one / num_two}")
        case _:
            print(f"ERROR: {math_type} is not a type of math that I have ever heard of!")
    
    print("would you like to keep doing math with me? [y/n]")
    should_quit = input(prompt)
    if should_quit == 'n':
        print("😭")
        is_running = False
    