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
11 to find factors
12 to check prime or not
13 to %
14 to prime factorize
15 to check if perfect square
16 to check if perfect cube
17 to find square root
18 to find perimeter of rectangle
19 to find perimeter of square
20 to find perimeter of perfect polygon
21 to find area of rectangle
22 to find area of trapezium
23 to find area of triangle if measure of base & height is known
24 to find area of triangle if measure of sides are known
25 to find amount/intrest for simple intrest
26 to find amount/intrest for compound intrest
27 to convert km/h to m/s
28 to convert m/s to km/h
29 to find speed
30 to find velocity
31 to find accelaration
32 to find a value using v = u + at
33 to find a value using s = ut + 1/2 * at
34 to find a value using 2as = v^2 - u^2
35 to find Lowest Common Multiple
36 to find Common Factors
37 to find prime numbers between two numbers
38 to find Force\n'''))
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
        no = float(input('Number: '))
        po = float(input('Power: '))
        pow(no,po)

    elif user_input == 6:
        no = float(input('Number: '))
        square(no)
        print('...............................................\n')

    elif user_input == 7:
        no = float(input('Number: '))
        cube(no)
        print('...............................................\n')

    elif user_input == 8:
        no = float(input('Number: '))
        evenodd(no)
        print('...............................................\n')

    elif user_input == 9:
        no1 = float(input('Number 1: ')) 
        no2 = float(input('Number 2: '))
        greater(no1,no2)
        print('...............................................\n')

    elif user_input == 10:
        no = float(input('Number: '))
        div = float(input('Divisor: '))
        divisible(no,div)
        print('...............................................\n')

    elif user_input == 11:
        no = int(input('Number: '))
        factors(no)
        print('...............................................\n')

    elif user_input == 12:
        no = int(input('Number: '))
        ans = isprime(no)
        if ans == True:
            print(f'{num} is prime')
        else:
            print(f'{num} is not prime')
        print('...............................................\n')

    elif user_input == 13:
        pc = float(input('Percentage: '))
        no = float(input('Number: '))
        percent(no,pc)
        print('...............................................\n')

    elif user_input == 14:
        no = float(input('Number: '))
        primefac(no)
        print('\n...............................................\n')

    elif user_input == 15:
        no = float(input('Number: '))
        issquare(no)
        print('\n...............................................\n')

    elif user_input == 16:
        no = float(input('Number: '))
        iscube(no)
        print('\n...............................................\n')
    
    elif user_input == 17:
        no = float(input('Number: '))
        print(sqrt(no))
        print('\n...............................................\n')
    
    elif user_input == 18:
        length = float(input('Length: ')) 
        breadth = float(input('Breadth: '))
        rectperi(length, breadth)

    elif user_input == 19:
        side = float(input('Side: '))
        sqperi(side)

    elif user_input == 20:
        no = float(input('Number of sides: '))
        length = float(input('Length of sides: '))
        perfpolyperi(no, side)

    elif user_input == 21:
        length = float(input('Length: ')) 
        breadth = float(input('Breadth: '))
        arearect(length, breadth)

    elif user_input == 22:
        h = float(input('Height: '))
        a =  float(input('Length of 1st parallel side: '))
        b =  float(input('Length of 2nd parallel side: '))
        areatrap(h, a, b)

    elif user_input == 23:
        height = float(input('Height: '))
        base = float(input('Base: '))
        areatri(height, base)

    elif user_input == 24:
        a = float(input('Side A: '))
        b = float(input('Side B: '))
        c = float(input('Side C: '))
        areatri_h(a,b,c)

    elif user_input == 25:
        p = float(input('Principal: '))
        r = float(input('Rate: '))
        t = float(input('time: '))
        simintrest(p, r, t)

    elif user_input == 26:
        p = float(input('Principal: '))
        r = float(input('Rate: '))
        t = float(input('time(in year): '))
        comintrest(p, r, t)
    
    elif user_input == 27:
        km = float(input('km: '))
        M_s(km)

    elif user_input == 28:
        m = float(input('m:'))
        Km_h(m)
        
    elif user_input == 29:
        s = float(input('distance(m): '))
        t = float(input('time(sec): '))
        speed(s,t)
        
    elif user_input == 30:
        s = float(input('displacement(m): '))
        t = float(input('time(sec): '))
        vel(s,t)

    elif user_input == 31:
        u = float(input('intial velovity(m/s): '))
        v = float(input('final velovity(m/s): '))
        t = float(input('time(sec): '))
        xlr8(v,u,t)

    elif user_input == 32:
        first_eq()

    elif user_input == 33:
        second_eq()

    elif user_input == 34:
        third_eq()

    elif user_input == 35:
        num1 = int(input('Number 1:'))
        num2 = int(input('Number 2:'))
        lcm(num1,num2)

    elif user_input == 36:
        num1 = int(input('Number 1:'))
        num2 = int(input('Number 2:'))
        comfac(num1,num2)

    elif user_input == 37:
        num1 = int(input("Number 1: "))
        num2 = int(input("Number 2: "))
        numbers = primeNoBetween(num1, num2)
        if numbers != False:
            print(numbers)
            print(f"Total number of prime number between {num1} and {num2} are {len(numbers)}")
        else:
            print("both numbers are equal")
    elif user_input == 38:
        force()

    else:
        print('Not a valid No.\n')
        print('...............................................\n')
        q = input('Press q to quit: ')

# 😃
