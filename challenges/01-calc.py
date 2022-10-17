# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

result = input(f"what method would you like to use a.)multiply b.)divide c.)add d.)subtract")

print (result)

def getValue():
    value1 = input("what is number 1 : ")
    value2 = input("what is number 2 : ")

    return [value1,value2]


match result:
    case "multiply":
        print("you are in multiply")
        arr_of_values =getValue()
        print ( int(arr_of_values[0]), "*", int(arr_of_values[1]) , " = ", int(arr_of_values[0])*int(arr_of_values[1]))

    case "divide":
        print("you are in divide")
        arr_of_values =getValue()
        print ( int(arr_of_values[0]), "/", int(arr_of_values[1]) , " = ", int(arr_of_values[0])/int(arr_of_values[1]))
    case "add":
        print("you are in addition")
        arr_of_values =getValue()
        print ( int(arr_of_values[0]), "+", int(arr_of_values[1]) , " = ", int(arr_of_values[0])+int(arr_of_values[1]))
    case "subtract":
        print("you are in subtraction")
        arr_of_values =getValue()
        print ( int(arr_of_values[0]), "-", int(arr_of_values[1]) , " = ", int(arr_of_values[0])-int(arr_of_values[1]))
    case _:
        print("that is not accepted here find another calculator")
    