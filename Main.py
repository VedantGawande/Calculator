from Calculator import *
q = ''
user_input = 0
def user():
    global user_input
    try:
        user_input = int(input('''Press 1 to add
2 to sub
3 to multiply
4 to divide
5 to power
6 to square
7 to cube
8 to check even or odd
9 to check greater or smaller
10 to check divisiblity
11 to show factors
12 to check prime or not
13 to %
14 to prime factorize
15 to check if perfect square
16 to check if perfect cube
17 to show square root
18 to find perimeter of rectangle
19 to find perimeter of square
20 to find perimeter of perfect polygon
21 to find area of rectangle
22 to find area of trapezium
23 to find area of triangle if measure of base & height is known
24 to find area of triangle if measure of sides are known
25 to find amount/intrest for simple intrest
26 to find amount/intrest for compound intrest\n'''))
        print('')
        invalid = False
    except:
        print('Invalid input\n')
        print('...............................................')
        invalid = True
        if invalid:
            user()
while q.lower() != 'q':
    print('...............................................\n')
    user()
    lst = []
    if user_input == 1:
        no = int(input('How many numbers do you want to add? '))
        no += 1
        ans = 0
        for i in range(1,no):
            num = int(input(f'Number {i}: '))
            lst.append(num)
        add(lst)
        print('...............................................\n')
            # ans = ans + num
            # print(ans)
    elif user_input == 2:
        print('First input the number then input the numbers you want to subtract\n')
        no = int(input('How many numbers do you want to subtract with the first number? '))
        no += 1
        ans = 0
        for i in range(0,no):
            if i == 0:
                num = int(input(f'First number: '))
                lst.append(num)
            else:
                num = int(input(f'Number {i}: '))
                lst.append(num)
        sub(lst)
        print('...............................................\n')
    elif user_input == 3:
        no = int(input('How many numbers do you want to multiply? '))
        no += 1
        ans = 0
        for i in range(1,no):
            num = int(input(f'Number {i}: '))
            lst.append(num)
        mul(lst)
        print('...............................................\n')
    elif user_input == 4:       
        no = int(input('How many numbers do you want to divide with divisor? '))
        no += 1
        print('First input the number then input divisors\n')
        ans = 0
        for i in range(0,no):
            if i == 0:
                num = int(input('Number: '))
                lst.append(num)
            else:
                num = int(input(f'Divisor {i}: '))
                lst.append(num)
        div(lst)
        print('...............................................\n')
    elif user_input == 5:
        print('First input the number then input the power')
        no = int(input('Number: '))
        po = int(input('Power: '))
        pow(no,po)
    elif user_input == 6:
        no = int(input('Number: '))
        square(no)
        print('...............................................\n')
    elif user_input == 7:
        no = int(input('Number: '))
        cube(no)
        print('...............................................\n')
    elif user_input == 8:
        no = int(input('Number: '))
        evenodd(no)
        print('...............................................\n')
    elif user_input == 9:
        no1 = int(input('Number 1: ')) 
        no2 = int(input('Number 2: '))
        greater(no1,no2)
        print('...............................................\n')
    elif user_input == 10:
        no = int(input('Number: '))
        div = int(input('Divisor: '))
        divisible(no,div)
        print('...............................................\n')
    elif user_input == 11:
        no = int(input('Number: '))
        factors(no)
        print('...............................................\n')
    elif user_input == 12:
        no = int(input('Number: '))
        isprime(no)
        print('...............................................\n')
    elif user_input == 13:
        pc = int(input('Percentage: '))
        no = int(input('Number: '))
        percent(no,pc)
        print('...............................................\n')
    elif user_input == 14:
        no = int(input('Number: '))
        primefac(no)
        print('\n...............................................\n')
    elif user_input == 15:
        no = int(input('Number: '))
        issquare(no)
        print('\n...............................................\n')
    elif user_input == 16:
        no = int(input('Number: '))
        iscube(no)
        print('\n...............................................\n')
    
    elif user_input == 17:
        no = int(input('Number: '))
        print(sqrt(no))
        print('\n...............................................\n')
    
    elif user_input == 18:
        length = int(input('Length: ')) 
        breadth = int(input('Breadth: '))
        rectperi(length, breadth)

    elif user_input == 19:
        side = int(input('Side: '))
        sqperi(side)

    elif user_input == 20:
        no = int(input('Number of sides: '))
        length = int(input('Length of sides: '))
        perfpolyperi(no, side)

    elif user_input == 21:
        length = int(input('Length: ')) 
        breadth = int(input('Breadth: '))
        arearect(length, breadth)

    elif user_input == 22:
        h = int(input('Height: '))
        a =  int(input('Length of 1st parallel side: '))
        b =  int(input('Length of 2nd parallel side: '))
        areatrap(h, a, b)

    elif user_input == 23:
        height = int(input('Height: '))
        base = int(input('Base: '))
        areatri(height, base)

    elif user_input == 24:
        a = int(input('Side A: '))
        b = int(input('Side B: '))
        c = int(input('Side C: '))
        areatri_h(a,b,c)

    elif user_input == 25:
        p = float(input('Principal: '))
        r = float(input('Rate: '))
        t = float(input('time: '))
        simintrest(p, r, t)

    elif user_input == 26:
        p = float(input('Principal: '))
        r = float(input('Rate: '))
        t = float(input('time: '))
        comintrest(p, r, t)

    else:
        print('Not a valid No.\n')
        print('...............................................\n')
        q = input('Press q to quit: ')

# Update includes -
# Geometry operations
# Simple Intrest
# Compound Intrest
