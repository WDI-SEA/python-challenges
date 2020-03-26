# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

operators = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div
}

def transform(str):
    str = str.lower()
    str = str.strip()
    return str

def get_operator():
    operator = input("What calculation would you like to do? (add, sub, mult, div) ")
    operator = transform(operator)
    if operator in operators:
        return operator
    else:
        return None

def get_operand(num):
    operand = input(f"What is number {num} ")
    return int(operand)

operator = get_operator()
operand1 = get_operand(1)
operand2 = get_operand(2)

result = operators[operator](operand1, operand2)

print(f"Your result is {result}")