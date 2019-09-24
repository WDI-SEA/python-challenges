
inString = input(f'String to reverse:\n')

strArr = []
for letter in inString:
  strArr.append(letter)

strArr.sort()
print (''.join(map(str, strArr)))
