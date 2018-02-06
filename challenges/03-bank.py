

bal = 3000


print('your current balance is', bal)
meth = input('What would you like to do? (dep, with, bal)\n')

if (meth == 'dep'):
  dep_amount = input('How much?')
  if dep_amount == '':
    print('you must input an integer')
  else:
    dep_amount = int(dep_amount)
    bal = bal + dep_amount
elif (meth == 'with'):
  with_amount = input('How much?')
  if with_amount == '':
    print('you must input an integer')
  else:
    with_amount = int(with_amount)
    bal = bal - with_amount
elif (meth == 'bal'):
  print('your current balance is', bal)
else:
  print('invalid query')

print('your balance is now at', bal)
