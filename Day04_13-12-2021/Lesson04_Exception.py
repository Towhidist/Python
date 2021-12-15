while true:
    print('Main Menu')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Divition')
    print('5. Exit')
    print('Enter your Selection :', end='')

    x=input()
    if x=='1':
        a=int(input('a : '))
        b=int(input('b : '))
        print('Addition is %s'%(a+b))
    elif x=='2':
        print('Subtraction')
    elif x=='3':
        print('Multiplication')
    elif x=='4':
        print('Divition')
    elif x=='5':
        print('Good Bye')
        break
    else:
        print('Invalid Selection')