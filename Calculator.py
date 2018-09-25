def calculation():
    cal = input('What calculation would you like to do? (add, sub, mult, div)')
    try:
        num1 = int(input('What is the number 1?'))
        num2 = int(input('What is the number 2?'))
    except:
        print('It is not a number')
    result = 0;
    if (cal == 'add'):
        result = num1 + num2
    elif (cal == 'sub'):
        result = num1 - num2
    elif (cal == 'mult'):
        result = num1*num2
    elif (cal == 'div'):
        result = num1/num2
    
    
    print('Your result is: ', result);
