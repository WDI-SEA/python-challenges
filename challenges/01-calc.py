# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# is_running = True

# while is_running:
#     operation = input("Which calculation would you like to do? (add, sub, mult, div) \n")
#     num1 = float(input("what is number 1? \n"))
#     num2 = float(input("what is number 2? \n"))

#     if operation == 'add':
#         result = num1 + num2
#     elif operation == 'sub':
#         result = num1 - num2
#     elif operation == 'mult':
#         result = num1 * num2
#     elif operation == 'div':
#         if num2 != 0:
#             result = num1 / num2
#         else:
#             print("IMPOSSIBLE to divide by ZERO")
#     else:
#         print("That wasn't an option... (add, sub, mult, div)")
#     print(f"Your result is {result}.")

#     done = input("Do another calculation? (yes, no)\n")
#     if done.lower() == "no":
#         break

is_running = True

while is_running:
    # display math choices and ask user to choose one
    prompt = "> "
    print("Hello, user")
    print("What kind of math would you like to do?")
    print("add, sub, mul, div?")
    math_choice = input(prompt)
    print (f"math choice: {math_choice}")

    #ask the user to input two numbers, one by one
    print("Enter the first number to use.")
    number_one = input(prompt)
    print("Now the second number.")
    number_two = input(prompt)

    print(number_one, number_two)

    try:
        # convert input to integers
        number_one = int(number_one)
        number_two = int(number_two)

        # dictionary switch
        switch = {
            "add": number_one + number_two,
            "sub": number_one - number_two, 
            "mul": number_one * number_two,
            "div": number_one / number_two
        }

        if math_choice in switch:
            print(f'result: {switch[math_choice]}')
        else:
        #default for the switch case
            print(f"I lied, {math_choice} isn't a math I know about!")

    except ValueError as e:
        print("That wasn't a real number!")

    # ask the user if they would like to exit
    print("Would you like to continue doing math? (y/n)\n")
    should_quit = input(prompt)
    if should_quit == "n":
        is_running = False

    
    

