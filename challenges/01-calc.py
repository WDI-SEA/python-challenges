# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calc():
  # info messgae
  print('I can do the following maths for you: addition, subtraction, multiplacation or division.\nPlease entera add, sub, mult, div to do a math!')

  # get math type and remove whitespace
  math = input('please select a math:')
  math = math.strip()

  # get numbers and restart on bad inputs
  number_one = input('please select your first number:')
  try:
    number_one = float(number_one)
  except ValueError:
    print(f'I know a number when I see one, and \'{number_one}\' is definately not a number!\nPlease Try again.\n~~~~~~~~~~~')
    calc()

  number_two = input('please select your second number:')
  try:
    number_two = float(number_two)
  except ValueError:
    print(f'You can\'t fool me! I know that \'{number_two}\' is definately not a number!\nPlease Try again.\n~~~~~~~~~~~')
    calc()
  
  # do some math
  switch = {
    'add': number_one + number_two,
    'sub': number_one - number_two,
    'mult': number_one * number_two,
    'div': number_one / number_two
  }
  result = switch.get(math)

  # display result or restart
  if result is not None:
    print(f'Here is the math you ordered: {result}\n~~~~~~~~~~~')
  else:
    print(f'I\'ve never heard of a math called \'{math}\' before!\nPlease Try again.\n~~~~~~~~~~~')
    calc()
  
calc()