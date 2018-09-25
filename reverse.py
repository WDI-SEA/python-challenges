def reverseme():
    string = input('Enter a string to reverse: ')
    reverse = ''
    for s in range(0,-len(string),-1):
        print(reverse)
        print(s)
        reverse = reverse + string[s-1]
    print(reverse)


reverseme()