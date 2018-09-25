def calculator():
    choice = input('What calculation would you like to do? (add, sub, mult, div)\n')
    num1 = int(input('What is number 1?\n'))
    num2 = int(input('What is number 2?\n'))

    if(choice == 'add'):
        answer = num1 + num2
    elif(choice == 'sub'):
        answer = num1 - num2
    elif(choice == 'mult'):
        answer = num1 * num2
    elif(choice == 'div'):
        answer = num1 / num2
    else:
        print('This is not math. This is madness.')
        return 

    print('Your result is {}'.format(answer))

calculator()