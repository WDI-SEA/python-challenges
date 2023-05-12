# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

is_running = True

while is_running:
    # display math choices and ask user to chose one
    prompt = ">"
    print("Hello, User🙋‍♂️")
    print("Tell me what kind of math you would like to do")
    print("possible choices: add, sub, mul, div")
    math_choice = input(prompt)
    print(f"math choice: {math_choice}")


    # ask the user to input two numbers
    print ("Excellent math choice! Enter the first number to use")
    number_one = input(prompt)
    print("Now, enter a second Number")
    number_two = input(prompt)

    try:
    # convert input to integers
      number_one = int(number_one)
      number_two = int(number_two)

        # if/elif/else
      # og dictionary switch
      switch = {
        "add": number_one + number_two,
        "sub": number_one - number_two,
        "mul": number_one * number_two,
        "div": number_one / number_two
      }

      if math_choice in switch:
        print(f"result: {switch[math_choice]}")
      else:
        #  defualt for the switch case
        print(f"I lied, {math_choice} isn't a math I know about")

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
            print(f"{number_one} makes no sense to me! ")
            
    except ValueError as e:
      #  handle error instead of crashing
       print("That wasn't a real number!")


    # ask the user if they would like to exit
    print("would you like to contine doin math with me [y/n]?")
    should_quit = input(prompt)
    if should_quit == "n":
       is_running = False