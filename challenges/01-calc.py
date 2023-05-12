# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
# user_input = input("Please enter a number: ")
# if user_input.isdigit():
#     number = int(user_input)
# else:
#     print("That was not a valid number.")
#     exit()
# result = number + 5
# print("The result is:", result)

# value= input('the user will see this is the terminal')
is_running = True

while is_running:
    # display math choices and ask user to choose one
    prompt = ">"
    print("Hello, user 👋")
    print("Tell me what kind of math you would like to do")
    print("Possible choices: add, sub, mul, div")
    math_choice = input(prompt)
    # print(f"math choice: {math_choice}")

    # ask user to input two numbers, one by
    print("Excellent math choice! Enter the first number")
    number_one = input(prompt)
    print("Now, enter a second number")
    number_two = input(prompt)

    # print(number_one, number_two)
    try:
    # convert input to integers
        number_one = int(number_one)
        number_two = int(number_two)

    # if/elif/else
    # og dictionary switch
        # switch = {
        #     "add": number_one + number_two,
        #     "sub": number_one - number_two,
        #     "mul": number_one * number_two,
        #     "div": number_one / number_two
        # }

        # if math_choice in switch:
        #     print(f"result: {switch[math_choice]}")
        # else:
        #     # default for switch case
        #     print(f"I lied, {math_choice} isn't a math choice I know about!")

        # match case (new python switch)
        match math_choice:
            case "add":
                print(f"{number_one} + {number_two} = {number_one + number_two}")
            case "sub":
                print(f"{number_one} - {number_two} = {number_one - number_two}")
            case "mul":
                print(f"{number_one} * {number_two} = {number_one * number_two}")
            case "div":
                print(f"{number_one} / {number_two} = {number_one / number_two}")
            case _:
                print(f"{math_choice} makes no sense to me!")
    except ValueError as e :
        # handle error instead of crashing
        print("That wasn't a real number 😿")
    
    # ask user if they would like to exit
    print("would you like to countinue doing math with me [y/n]?")
    should_quit = input(prompt)
    if should_quit == "n":
        is_running = False
