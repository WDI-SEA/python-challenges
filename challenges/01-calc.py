# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# input() for type of calc (add, sub, mult, div)
calc = input('Welcome to calculator! What kind of calculation would you like to do? (add, subtract, multiply, divide)\n')
print(f'Okay cool, so you want to {calc}')

first_num = input('What is the first number you want to use?\n')
print(f'Alrighty then, your first number is {first_num}')
first_num = int(first_num)

second_num = input('What is the second number you want to use?\n')
print(f'Awesome, so your second number is {second_num}. Just give me a second while I think...')
second_num = int(second_num)

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

