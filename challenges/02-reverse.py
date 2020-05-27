# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

def reverseString(str):
      var = ''
      # print(len(str))
      for i in range(len(str)-1, -1,-1):
          var = var+ str[i]
         # print(str[i])
      return var
  
   
str1 = reverseString("ideh")

#reverseString("readme")

print("reverse:",str1)

 
str2 = "".join(reversed("Hello Yello Pretty fellow"))
print(str2)


input = "hello world"
result = ''
for c in input:
      result = c + result
print(result)