def Calculator():
    methods = ['addition', 'subtraction', 'multiplication', 'division']
    print(methods)
    
    method = input('what method they would like to use: ')
    if method in methods:
        input1 = input('What is number 1? ')
        input2 = input('What is number 2? ')
        input1 = int(input1)
        input2 = int(input2)
        if method=='addition':
            ans = input1+input2
            print(f'Your result is {ans}')
        elif method=='subtraction':
            ans = input1-input2
            print(f'Your result is {ans}')                 
        elif method=='multiplication':
            ans = input1*input2
            print(f'Your result is {ans}')             
        else:
            ans = input1/input2
            print(f'Your result is {ans}')    

Calculator()