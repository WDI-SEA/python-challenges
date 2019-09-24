
s = input('String: \n')
rs = []
for letter in s:
  rs.insert(0,letter)
print (''.join(map(str, rs)))
