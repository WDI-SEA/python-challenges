binarySearch(sortedArr, targetValue)
min = 0
max = sortedArr.length -1
guess = Math.floor(min+max/2)

while(min <= max):
	new guess
	if(sortedArr[guess] == target):
		return guess
	elif(sortedArr[guess] < target):
		min = guess+1
	else:
		max = guess -1
return -1