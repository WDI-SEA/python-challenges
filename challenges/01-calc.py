# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
input1 = input('What would you like to do? ')
input1 = input1.lower()

if input1 == 'addition':
    def addition():
        print('You chose addition')
        num1 = input('First Number:')
        num1 = int(num1)
        num2 = input('Second Number:')
        num2 = int(num2)
        sum = num1 + num2
        print(f'Your sum is: {sum}')
    addition()

elif input1 == 'subtraction':
    def subtraction():
        print('You chose subtraction')
        num1 = input('First Number:')
        num1 = float(num1)
        num2 = input('Second Number:')
        num2 = float(num2)
        difference = num1 - num2
        print(f'Your difference is: {difference}')
    subtraction()

elif input1 == 'multiplication':
    def multiplication():
        print('You chose multiplication')
        num1 = input('First Number:')
        num1 = float(num1)
        num2 = input('Second Number:')
        num2 = float(num2)
        product = num1 * num2
        print(f'Your product is: {product}')
    multiplication()

elif input1 == 'division':
    def division():
        print('You chose division')
        num1 = input('First Number:')
        num1 = float(num1)
        num2 = input('Second Number:')
        num2 = float(num2)
        quotient = num1 / num2
        print(f'Your quotient is: {quotient}')
    division()
