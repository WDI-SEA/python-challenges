# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
user_string = input("Give me a string to alphabetize: ")
str_list = list(user_string)
n = len(str_list)
for i in range(0, n-1):
	min_letter = str_list[i]
	r = 0
	for j in range(i+1,n):
		if(str_list[j] <= min_letter):
			min_letter = str_list[j] 
			r = j
			temp = str_list[i]
			str_list[i] = min_letter
			str_list[r] = temp
final_string = ""
for i in range(n):
	final_string = final_string + str_list[i]
print(final_string)