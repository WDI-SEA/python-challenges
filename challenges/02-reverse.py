# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#

should_run = True

while should_run:
    print("hello user, give me a string! (enter q to quit)")

    string = input()

    if string == 'q':
        should_run = False

    new_string = ''

    for char in string:
    new_string = char + new_string

    print(new_string)

