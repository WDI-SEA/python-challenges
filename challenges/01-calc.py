
def calc(op, x, y):
  if op == 'add':
    return x + y
  elif op == 'sub':
    return x - y
  elif op == 'div':
    return x / y
  elif op == 'mult':
    return x * y
  else:
    return 'Unknown operator.'

op = input('What do you want to do? (add, sub, div, mult)\n')
x = int(input('What is the first number?\n'))
y = int(input('What is the second number?\n'))

print(f'Result: {calc(op, x, y)}')

